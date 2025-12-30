from django.db import models


class DescriptiveModel(models.Model):
    description = models.TextField(blank=True)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created"]
