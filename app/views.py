from django.http import HttpResponse
from rest_framework import viewsets

from app.models import Request, Response
from app.serializers import RequestSerializer, ResponseSerializer


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


class ResponseViewSet(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()


def index(req):
    return HttpResponse("hello world")
