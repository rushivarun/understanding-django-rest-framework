from django.db import models
from django.contrib.auth.models import User


class questions(models.Model):
    question = models.TextField()
    status = models.CharField(default='inactive', max_length=10)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
