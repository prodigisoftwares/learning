from django.db import models

from .abstract import TimestampedModel


class Exam(TimestampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Exam"
        verbose_name_plural = "Exams"

    def __str__(self):
        return self.title


class Topic(TimestampedModel):
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


class TestBank(TimestampedModel):
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
