from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username} - {self.email}"


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=64)
    description = models.TextField()
    bid = models.IntegerField()
    img_url = models.URLField()
    category = models.CharField(max_length=64, null=False, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.bid} - {self.img_url[:20]}"

