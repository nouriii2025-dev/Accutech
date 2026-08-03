from django.db import models


class ChatLog(models.Model):
    """Optional audit trail of chatbot exchanges, useful for improving intents."""

    session_key = models.CharField(max_length=64, blank=True, db_index=True)
    user_message = models.TextField()
    bot_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"[{self.created_at:%Y-%m-%d %H:%M}] {self.user_message[:40]}"
