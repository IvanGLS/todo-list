from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models



class User(AbstractUser):
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name

class Task(models.Model):
    content = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True)
    tags = models.ManyToManyField(Tag,
                                 related_name="tasks", )

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return "{}".format(self.content)