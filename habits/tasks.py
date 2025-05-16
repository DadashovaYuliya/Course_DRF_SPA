import requests
from celery import shared_task

from config import settings
from habits.models import Habit


@shared_task
def send_message(pk):
    """Отправляет напоминание пользователю о привычке."""
    habit = Habit.objects.get(pk=pk)
    message = (
        f"Напоминание! Выполните полезную привычку {habit.name} в месте {habit.place}."
        f"После этого порадуйте себя: {habit.reward if habit.reward else habit.related_habit}"
    )
    params = {
        "text": message,
        "chat_id": habit.user.tg_chat_id,
    }
    requests.get(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params)
