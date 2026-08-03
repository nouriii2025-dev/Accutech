from rest_framework import serializers


class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField(allow_blank=True, max_length=1000)


class ChatReplySerializer(serializers.Serializer):
    reply = serializers.CharField()
    quick_replies = serializers.ListField(child=serializers.CharField())
