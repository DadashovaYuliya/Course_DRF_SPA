from django.db import models

from users.models import User


class Habit(models.Model):

    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="habits", null=True, blank=True
    )
    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.DateTimeField(
        verbose_name="Время",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100, verbose_name="Действие")
    is_pleasant_habit = models.BooleanField(verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="related_habits",
        verbose_name="Связанная привычка",
        blank=True,
        null=True,
    )
    recurrence_days = models.PositiveIntegerField(default=1, verbose_name="Периодичность в днях")
    reward = models.CharField(
        max_length=100,
        verbose_name="Вознаграждение",
        blank=True,
        null=True,
    )
    time_to_complete = models.PositiveIntegerField(blank=True, null=True, verbose_name="Время на выполнение в минутах")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")
    notified = models.BooleanField(default=False, verbose_name="Уведомление отправлено")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.name} ({'приятная' if self.is_pleasant_habit else 'полезная'})"
