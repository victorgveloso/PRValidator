from django.http import HttpResponse
from rest_framework import viewsets

from app.models import Request, Response
from app.serializers import RequestSerializer, ResponseSerializer


class FieldsFilterMixin(viewsets.ModelViewSet):
    def ignore_nested_field_access(self, r):
        return r.split("__")[0]

    def extract_fields(self, d: dict):
        field_names = [i.name for i in self.serializer_class.Meta.model._meta.get_fields() if hasattr(i, 'name')]
        return {k: v for k, v in d.items() if self.ignore_nested_field_access(k) in field_names}

    def get_queryset(self):
        return self.queryset.filter(**self.extract_fields(self.request.query_params.dict()))


class RequestViewSet(FieldsFilterMixin):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


class ResponseViewSet(FieldsFilterMixin):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()


def index(req):
    return HttpResponse("hello world")
