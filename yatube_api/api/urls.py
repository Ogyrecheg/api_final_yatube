from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet

router_v1 = SimpleRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')


urlpatterns = [
    path('v1', include('djoser.urls.jwt')),
]
