import requests

from core.settings import BOT_TOKEN
from user.models import User


class NotificationService:
    def __init__(self, message):
        self.message = message

    users = None

    def notify(self) -> dict:
        self.users = User.objects.filter(tg_id__isnull=False)

        for user in self.users:
            self.send_message_telegram(tg_id=user.tg_id)

        return {"ok": True, "count": self.users.count()}

    def send_message_telegram(self, tg_id):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={tg_id}&text={self.message}"
        requests.get(url=url)
