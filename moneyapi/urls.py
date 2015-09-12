from rest_framework import routers
from django.conf.urls import include, url
from . import views

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
