from abc import ABC, abstractmethod

import requests

from core.settings import BOT_TOKEN


class NotificationSender(ABC):
    @abstractmethod
    def send(self):
        pass


class TelegramSender(NotificationSender):
    def __init__(self, chat_id: int, text: str):
        self.chat_id = chat_id
        self.text = text

    def send(self):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={self.chat_id}&text={self.text}"
        return requests.get(url=url)


class EmailSender(NotificationSender):
    def __init__(self, mail: str, title: str, body: str):
        self.mail = mail
        self.title = title
        self.body = body

    def send(self):
        print("какой то мейл код рассылки")
        return {"ok": True, "count": 1}


class NotificationService:
    def __init__(self, senders: [NotificationSender]):
        self.senders = senders

    def send(self):
        for sender in self.senders:
            sender.send()
        return
