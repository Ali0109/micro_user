from rest_framework import serializers


class NotifySerializer(serializers.Serializer):
    message = serializers.CharField()
