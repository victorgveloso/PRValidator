from django.http import HttpResponse
from rest_framework import viewsets

from app.models import Request, Response
from app.serializers import RequestSerializer, ResponseSerializer


class FieldsFilterMixin(viewsets.ModelViewSet):
    def extract_fields(self, d: dict):
        return {k: v for k, v in d.items() if k in self.serializer_class.Meta.model._meta.fields}

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
