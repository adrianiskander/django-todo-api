from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=128)
    is_done = models.BooleanField(default=False)
