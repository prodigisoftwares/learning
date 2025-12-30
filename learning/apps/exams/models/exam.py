from django.db import models

from .abstract import DescriptiveModel, TimestampedModel


class Exam(DescriptiveModel, TimestampedModel):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Exam"
        verbose_name_plural = "Exams"

    def __str__(self):
        return self.title


class Topic(DescriptiveModel, TimestampedModel):
    exam = models.ForeignKey(
        Exam,
        related_name="topics",
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.name


class TestBank(DescriptiveModel, TimestampedModel):
    exam = models.ForeignKey(
        Exam,
        related_name="banks",
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Test Bank"
        verbose_name_plural = "Test Banks"

    def __str__(self):
        return self.name
