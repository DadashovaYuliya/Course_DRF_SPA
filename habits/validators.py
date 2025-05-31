from rest_framework.serializers import ValidationError


def validate_fields(habit):
    if habit.reward and habit.related_habit:
        raise ValidationError("Нельзя одновременно указывать связанную привычку и вознаграждение")
    if habit.is_pleasant_habit:
        if habit.reward:
            raise ValidationError("Приятная привычка не может иметь вознаграждение.")
        if habit.related_habit:
            raise ValidationError("Приятная привычка не может иметь связанную привычку.")
    if habit.related_habit and not habit.related_habit.is_pleasant_habit:
        raise ValidationError("Связанная привычка должна быть приятной.")


def validate_periodicity(recurrence_days):
    if recurrence_days < 7:
        raise ValidationError("Периодичность должна быть не менее 7 дней.")
    elif recurrence_days > 7:
        raise ValidationError("Необходимо выполнять привычку хотя бы раз в неделю.")


def validate_time_to_complete(time_to_complete):
    if time_to_complete * 60 > 120:
        raise ValidationError("Время выполнения не должно превышать 120 секунд.")
