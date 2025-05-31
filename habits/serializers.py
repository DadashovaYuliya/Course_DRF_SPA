from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_fields, validate_periodicity, validate_time_to_complete


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        habit_instance = self.instance or Habit()

        for attr, value in data.items():
            setattr(habit_instance, attr, value)

        validate_fields(habit_instance)

        recurrence_days = data.get("recurrence_days", getattr(self.instance, "recurrence_days", None))
        if recurrence_days is not None:
            validate_periodicity(recurrence_days)

        time_to_complete = data.get("time_to_complete", getattr(self.instance, "time_to_complete", None))
        if time_to_complete is not None:
            validate_time_to_complete(time_to_complete)

        return data


class PublicHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = (
            "name",
            "is_pleasant_habit",
        )
