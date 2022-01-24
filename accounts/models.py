from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_at']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback', 'sent_at')