from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    aproved = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username