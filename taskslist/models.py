from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

class Task(models.Model):
    content = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True)
    tag = models.ManyToManyField(Tag,
                                 related_name="tag", )

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return "{}".format(self.content)