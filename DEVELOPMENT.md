# Development Guide

## Project Structure

### Exam Models

The exam system is built with a modular model structure in `learning/apps/exams/models/`:

- **abstract.py** - `TimestampedModel` base class providing automatic `created` timestamp to all models
- **exam.py** - Core exam structures: `Exam`, `Topic`, `TestBank`
- **question.py** - Question hierarchy: `Chapter`, `Question`, `QuestionOption`
- **flashcard.py** - `AcronymFlashcard` for study materials

#### Model Relationships

```
Exam
├── Topics
│   └── Chapters
│       └── Questions
│           └── QuestionOptions
├── TestBanks
│   └── Questions
└── AcronymFlashcards
```

All models inherit from `TimestampedModel` which provides automatic ordering by creation date (newest first) and a `created` timestamp field.

### Admin Interface

Admin registration uses the decorator pattern (@admin.register) in `learning/apps/exams/admin/__init__.py`. Each model has a dedicated admin class with:

- Appropriate `list_display` fields for quick scanning
- `search_fields` for finding records
- Relationships properly displayed

## Coverage Configuration

### .coveragerc

A centralized coverage configuration file (`learning/.coveragerc`) defines:

- **Branch coverage** - Enabled for comprehensive coverage analysis
- **Omit patterns** - Excludes `config/settings.py` from coverage (environment-specific)
- **Exclude lines** - Automatically excludes:
  - Lines with `pragma: no cover` comments
  - `__str__()` methods
  - `__repr__()` methods

This eliminates the need for inline pragma comments in model methods, keeping code cleaner.

### Running Coverage

Via the pre-commit hook:

```bash
cd learning && poetry run coverage report -m
```

The simplified hook (without model/admin.py omissions) relies on `.coveragerc` configuration for consistency.

## Testing Exam Models

When creating tests for exam models:

1. Use Django's `TestCase` for database isolation
2. Models are properly importable from `exams.models`
3. All relationships (ForeignKey) are enforced at the database level
4. Timestamps are automatically set; don't need to be specified in tests

Example:

```python
from exams.models import Exam, TestBank, Question, QuestionOption

exam = Exam.objects.create(title="Security+")
test_bank = TestBank.objects.create(exam=exam, name="Practice Questions")
```
