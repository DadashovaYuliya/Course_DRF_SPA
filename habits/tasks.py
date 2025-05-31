from datetime import timezone, timedelta

import requests
from celery import shared_task
from rest_framework import response

from django.conf import settings
from habits.models import Habit


@shared_task
def send_message():
    """Отправляет напоминание пользователю о привычке."""
    now = timezone.now()
    time_start = now + timedelta(minutes=5)
    time_end = now + timedelta(minutes=10)

    habits = Habit.objects.select_related("user").filter(
        time__gte=time_start,
        time__lte=time_end,
        notified=False,
        user__tg_chat_id__isnull=False,
    )

    for habit in habits:
        message = (
            f"Напоминание! Выполните полезную привычку {habit.name} в месте {habit.place}."
            f"После этого порадуйте себя: {habit.reward if habit.reward else habit.related_habit}"
        )
        params = {
            "text": message,
            "chat_id": habit.user.tg_chat_id,
        }
        requests.get(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params)
        if response.status_code == 200:
            habit.notified = True
            habit.save(update_fields=["notified"])
