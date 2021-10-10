import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Request(models.Model):
    class ProgrammingLanguage(models.IntegerChoices):
        UNAVAILABLE = -1, _("Programming Language's info unavailable")
        OTHER = 0, _("Other programming language")
        JAVA = 1, _('Java')
        PYTHON = 2, _('Python')
        JAVASCRIPT = 3, _('JavaScript')
        PHP = 4, _('PHP')
        TYPESCRIPT = 5, _('TypeScript')
        CSHARP = 6, _('C#')
        CPLUSPLUS = 7, _('C++')
        C = 8, _('C')
        GO = 9, _('GoLang')
        RUBY = 10, _('Ruby')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_owner = models.CharField(max_length=99)
    project_repo = models.CharField(max_length=99)
    pull_request_id = models.IntegerField()
    comment_text = models.CharField(max_length=2000)
    language = models.IntegerField(choices=ProgrammingLanguage.choices, default=ProgrammingLanguage.UNAVAILABLE)
    classification = models.CharField(max_length=99, default=None, blank=True, null=True)

    def github_url(self):
        return f"https://github.com/{self.project_owner}/{self.project_repo}/pull/{self.pull_request_id}"


class Response(models.Model):
    UNDEFINED = -1
    TRUE_POSITIVE = 0
    FALSE_POSITIVE = 1
    UNSURE = 2
    DECISION_OPTIONS = [
        (TRUE_POSITIVE, "True Positive"),
        (FALSE_POSITIVE, "False Positive"),
        (TRUE_POSITIVE + UNSURE, "Possibly True Positive"),
        (FALSE_POSITIVE + UNSURE, "Possibly False Positive"),
        (UNDEFINED, "Nobody evaluated yet"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    comment_id = models.CharField(max_length=50)
    commit_hash = models.CharField(max_length=50)
    decision = models.IntegerField(choices=DECISION_OPTIONS, default=UNDEFINED)
    classification = models.CharField(max_length=99, default=None, blank=True, null=True)

    def comment_url(self):
        return f"{self.request.github_url()}#{self.comment_id}"


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_owner = models.CharField(max_length=99)
    project_repo = models.CharField(max_length=99)
    stars = models.IntegerField()
    forks = models.IntegerField()
    issues = models.IntegerField()
    pulls = models.IntegerField()

    class Meta:
        unique_together = ('project_owner', 'project_repo',)


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    login = models.CharField(max_length=99, unique=True)
    following = models.IntegerField()
    followers = models.IntegerField()
    sponsors = models.IntegerField()
    repositories = models.IntegerField()
