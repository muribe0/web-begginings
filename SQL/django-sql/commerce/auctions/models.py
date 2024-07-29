from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username} - {self.email}"


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    wishlistedBy = models.ManyToManyField(User, related_name="wishlist", blank=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.IntegerField(null=False, blank=True)
    bid = models.IntegerField()
    img_url = models.URLField()
    category = models.CharField(max_length=64, null=False, blank=True)
    open = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="won_listings", null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.bid} - {self.img_url[:20]} - {self.wishlistedBy}"


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.listing} - {self.amount}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.listing.title} - {self.content}"