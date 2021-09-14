from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers

from app import views

routerV1 = routers.DefaultRouter()
routerV1.register(r'requests', views.RequestViewSet, basename="v1-request")
routerV1.register(r'responses', views.ResponseViewSet, basename="v1-response")
routerV2 = routers.DefaultRouter()
routerV2.register(r'requests', views.RequestViewSet, basename="v2-request")
routerV2.register(r'responses', views.ResponseViewSet, basename="v2-response")

urlpatterns = [
    path(r'', views.index),
    path(r'v1/', include(routerV1.urls)),
    path(r'v2/', include(routerV2.urls)),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True))
]
