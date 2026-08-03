from rest_framework.decorators import api_view
from rest_framework.response import Response

from .bot import get_reply
from .models import ChatLog
from .serializers import ChatMessageSerializer, ChatReplySerializer


@api_view(["POST"])
def chat_api(request):
    """
    POST /api/chat/  {"message": "do you calibrate pressure gauges?"}
    -> {"reply": "...", "quick_replies": ["...", "..."]}
    """
    incoming = ChatMessageSerializer(data=request.data)
    incoming.is_valid(raise_exception=True)
    user_message = incoming.validated_data.get("message", "")

    result = get_reply(user_message)

    if not request.session.session_key:
        request.session.save()

    ChatLog.objects.create(
        session_key=request.session.session_key or "",
        user_message=user_message,
        bot_reply=result["reply"],
    )

    outgoing = ChatReplySerializer(result)
    return Response(outgoing.data)
