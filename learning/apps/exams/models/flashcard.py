from django.db import models

from .abstract import TimestampedModel
from .exam import Exam


class AcronymFlashcard(TimestampedModel):
    exam = models.ForeignKey(
        Exam,
        related_name="flashcards",
        on_delete=models.CASCADE,
    )

    front = models.TextField()
    back = models.TextField()

    class Meta:
        ordering = ["-created"]
        verbose_name = "Acronym Flashcard"
        verbose_name_plural = "Acronym Flashcards"

    def __str__(self):
        return self.front
