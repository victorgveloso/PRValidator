from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField

from app.mapper import extract_tenant_name
from app.models import Request, Response


class CustomHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    def get_fields(self):
        fields = super().get_fields()
        for field in fields.values():
            if isinstance(field, HyperlinkedRelatedField):
                tenant_name = extract_tenant_name(self.context['request'].get_full_path())
                field.view_name = f'{tenant_name}-{field.view_name}'
        return fields


class ResponseSerializer(CustomHyperlinkedModelSerializer):
    class Meta:
        model = Response
        fields = ["id", "request", "author", "comment_id", "commit_hash", "decision", "comment_url", "url", "created_at", "updated_at", "classification"]


class RequestSerializer(CustomHyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ["id", "project_owner", "project_repo", "pull_request_id", "comment_text", "language", "github_url", "url", "created_at", "updated_at", "classification"]
