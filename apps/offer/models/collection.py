from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=150)
    offers = models.ManyToManyField("Offer", related_name="collections")
