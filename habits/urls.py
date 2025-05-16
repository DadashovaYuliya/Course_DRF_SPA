from django.urls import path
from rest_framework import routers

from habits.apps import HabitsConfig
from habits.views import HabitsViewSet, PublicHabitListAPIView

app_name = HabitsConfig.name

router = routers.DefaultRouter()
router.register(r"", HabitsViewSet)

urlpatterns = [
    path("public-habits", PublicHabitListAPIView.as_view(), name="public-habit-list"),
] + router.urls
