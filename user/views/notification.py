from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers.notify import NotifySerializer
from user.services.notification import NotificationService


class UserNotificationAPIView(APIView):

    serializer_class = NotifySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = serializer.validated_data["message"]
        notification_service = NotificationService(message=message)
        notify_info = notification_service.notify()

        return Response(notify_info)
