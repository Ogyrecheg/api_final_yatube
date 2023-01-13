from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router_v1 = SimpleRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet)
#router_v1.register(r'follow', FollowViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')


urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
