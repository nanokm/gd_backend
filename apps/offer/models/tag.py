from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
