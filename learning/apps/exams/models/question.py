from django.db import models

from .abstract import TimestampedModel
from .exam import TestBank, Topic


class Chapter(TimestampedModel):
    topic = models.ForeignKey(
        Topic,
        related_name="chapters",
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"

    def __str__(self):
        return self.name


class Question(TimestampedModel):
    test_bank = models.ForeignKey(
        TestBank,
        related_name="questions",
        on_delete=models.CASCADE,
    )

    chapter = models.ForeignKey(
        Chapter,
        related_name="questions",
        on_delete=models.CASCADE,
    )

    text = models.TextField()

    class Meta:
        ordering = ["-created"]
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.text


class QuestionOption(TimestampedModel):
    question = models.ForeignKey(
        Question,
        related_name="choices",
        on_delete=models.CASCADE,
    )

    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    explanation = models.TextField(blank=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Question Option"
        verbose_name_plural = "Question Options"

    def __str__(self):
        return self.text
