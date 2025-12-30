from django.db import models

from .exam import Exam


class AcronymFlashcard(models.Model):
    exam = models.ForeignKey(
        Exam,
        related_name="flashcards",
        on_delete=models.CASCADE,
    )

    front = models.TextField()
    back = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Acronym Flashcard"
        verbose_name_plural = "Acronym Flashcards"

    def __str__(self):
        return self.front
