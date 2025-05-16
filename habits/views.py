from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPagination
from habits.serializers import HabitSerializer, PublicHabitSerializer
from users.permissions import IsOwner


class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (IsOwner,)

        return super().get_permissions()


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = PublicHabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
