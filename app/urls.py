from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers

from app import views


def generate_multitenant_router(version):
    router = routers.DefaultRouter()
    router.register(r'requests', views.RequestViewSet, basename=f"{version}-request")
    router.register(r'responses', views.ResponseViewSet, basename=f"{version}-response")
    router.register(r'mergecommit', views.MergeCommitViewSet, basename=f"{version}-mergecommit")
    return router


def generate_unversioned_routers():
    r = routers.DefaultRouter()
    r.register(r'users', views.UserViewSet)
    r.register(r'projects', views.ProjectViewSet)
    return r


urlpatterns = [
    path(r'', views.index),
    path(r'', include(generate_unversioned_routers().urls)),
    path(r'v1/', include(generate_multitenant_router("v1").urls)),
    path(r'v2/', include(generate_multitenant_router("v2").urls)),
    path(r'v3/', include(generate_multitenant_router("v3").urls)),
    path(r'v4/', include(generate_multitenant_router("v4").urls)),
    path(r'v5/', include(generate_multitenant_router("v5").urls)),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True))
]
