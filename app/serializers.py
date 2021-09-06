from rest_framework import serializers

from app.models import Request, Response


class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Response
        fields = ["id", "request", "author", "comment_id", "decision", "comment_url"]


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ["id", "project_owner", "project_repo", "pull_request_id", "comment_text", "language", "url"]
