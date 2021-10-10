from django.http import HttpResponse
from rest_framework import viewsets

from app.mixins import FieldsFilterMixin
from app.models import Request, Response, User, Project, MergeCommit
from app.serializers import RequestSerializer, ResponseSerializer, UserSerializer, ProjectSerializer, \
    MergeCommitSerializer


class RequestViewSet(FieldsFilterMixin):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


class ResponseViewSet(FieldsFilterMixin):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()


class MergeCommitViewSet(FieldsFilterMixin):
    serializer_class = MergeCommitSerializer
    queryset = MergeCommit.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


def index(req):
    return HttpResponse("hello world")
