from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'requests', views.RequestViewSet)
router.register(r'responses', views.ResponseViewSet)

urlpatterns = [
    path(r'', views.index),
    path(r'v1/', include(router.urls)),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True))
]
