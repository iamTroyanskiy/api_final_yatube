from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register((r'posts/(?P<post_id>\d+)/comments'), CommentViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
