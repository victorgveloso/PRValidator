from django.http import HttpResponse
from django.utils.datastructures import MultiValueDict
from rest_framework import viewsets

from app.models import Request, Response
from app.serializers import RequestSerializer, ResponseSerializer


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def get_queryset(self):
        kwargs = self.request.query_params.dict()
        if "page" in kwargs:
            kwargs.pop("page")
        return self.queryset.filter(**kwargs)


class ResponseViewSet(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()

    def get_queryset(self):
        kwargs = self.request.query_params.dict()
        if "page" in kwargs:
            kwargs.pop("page")
        return self.queryset.filter(**kwargs)


def index(req):
    return HttpResponse("hello world")
