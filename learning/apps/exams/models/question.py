from django.db import models

from .exam import TestBank


class Question(models.Model):
    test_bank = models.ForeignKey(
        TestBank,
        related_name="questions",
        on_delete=models.CASCADE,
    )

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.text


class QuestionOption(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="choices",
        on_delete=models.CASCADE,
    )

    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    explanation = models.TextField(blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Question Option"
        verbose_name_plural = "Question Options"

    def __str__(self):
        return self.text
