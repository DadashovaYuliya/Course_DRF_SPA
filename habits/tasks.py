from datetime import timezone, timedelta

import requests
from celery import shared_task
from rest_framework import response

from config import settings
from habits.models import Habit


@shared_task
def send_message(pk):
    """Отправляет напоминание пользователю о привычке."""
    now = timezone.now()
    time_start = now + timedelta(minutes=5)
    time_end = now + timedelta(minutes=10)

    habit = Habit.objects.filter(pk=pk, time__gte=time_start,
        time__lte=time_end, notified=False)

    for h in habit:
        if not habit.user.tg_chat_id:
            continue
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
            habit.save()
