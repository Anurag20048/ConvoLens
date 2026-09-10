from django.db import models

class Feedback(models.Model):
    bot_reply = models.TextField()
    rating    = models.BooleanField()  # True = 👍 , False = 👎
    created   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bot_reply[:40]} ({self.rating})"
