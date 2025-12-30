from django.db import models


class Exam(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Exam"
        verbose_name_plural = "Exams"

    def __str__(self):  # pragma: no cover
        return self.title


class TestBank(models.Model):
    exam = models.ForeignKey(
        Exam,
        related_name="banks",
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Test Bank"
        verbose_name_plural = "Test Banks"

    def __str__(self):  # pragma: no cover
        return self.name
