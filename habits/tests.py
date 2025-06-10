from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(email="test@test.com")
        self.habit = Habit.objects.create(
            place="Дома", name="Сделать зарядку", is_pleasant_habit=False, user=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Тестирование получения привычки."""
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.habit.name)

    def test_habit_create(self):
        """Тестирование создания привычки."""
        url = reverse("habits:habit-list")
        data = {
            "place": "На работе",
            "name": "Выпить стакан воды",
            "is_pleasant_habit": False,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """Тестирование изменения привычки."""
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        data = {"place": "В парке", "recurrence_days": 7}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "В парке")

    def test_habit_delete(self):
        """Тестирование удаления привычки."""
        url = reverse("habits:habit-detail", args=(self.habit.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Тестирование списка привычек."""
        url = reverse("habits:habit-list")

        response = self.client.get(url)
        data = response.json()

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": self.habit.place,
                    "time": None,
                    "name": self.habit.name,
                    "is_pleasant_habit": False,
                    "recurrence_days": 1,
                    "reward": None,
                    "time_to_complete": None,
                    "is_public": False,
                    "user": self.habit.user.id,
                    "notified": False,
                    "related_habit": None,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
