from django.db import models

from .abstract import DescriptiveModel, TimestampedModel
from .exam import Exam


class Deck(DescriptiveModel, TimestampedModel):
    exam = models.ForeignKey(
        Exam,
        related_name="decks",
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Deck"
        verbose_name_plural = "Decks"

    def __str__(self):
        return self.name


class AcronymFlashcard(TimestampedModel):
    deck = models.ForeignKey(
        Deck,
        related_name="acronym_flashcards",
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
