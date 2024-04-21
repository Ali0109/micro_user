from rest_framework import generics
from rest_framework.response import Response

from notification.services.notifications import NotificationService, TelegramSender, EmailSender
from user.models import User
from user.serializers.user import UserSerializer


class UserCreateAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(**serializer.validated_data)

        senders = []
        if user.tg_id:
            senders.append(TelegramSender(
                chat_id=user.tg_id,
                text="User was created successfully")
            )
        elif user.email:
            senders.append(EmailSender(
                mail=user.email,
                title="Successfully registered",
                body="User was created successfully")
            )
        NotificationService(senders=senders).send()

        serializer = self.serializer_class(user)
        return Response(serializer.data)
