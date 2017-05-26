from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=150)
    messages = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
