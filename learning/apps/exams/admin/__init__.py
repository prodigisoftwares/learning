from django.contrib import admin

from ..models import AcronymFlashcard, Exam, Question, QuestionOption, TestBank


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "is_active")
    search_fields = ("title",)


@admin.register(TestBank)
class TestBankAdmin(admin.ModelAdmin):
    list_display = ("name", "exam", "created")
    search_fields = ("name",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "test_bank", "created")
    search_fields = ("text",)


@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    search_fields = ("text",)


@admin.register(AcronymFlashcard)
class AcronymFlashcardAdmin(admin.ModelAdmin):
    list_display = ("front", "exam", "created")
    search_fields = ("front",)
