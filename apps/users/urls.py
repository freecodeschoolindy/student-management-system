from django.urls import path, include
from rest_framework_nested import routers

from .views import (
    UserViewSet, SubmissionsViewSet, CustomAuthToken, UserProfileViewSet
)

router = routers.SimpleRouter()
router.register(r'', UserViewSet)

assignments_router = routers.NestedSimpleRouter(router, r'', lookup='list')
assignments_router.register(
    r'submissions',
    SubmissionsViewSet,
    basename='submissions'
)

profile_router = routers.NestedSimpleRouter(router, r'', lookup='list')
profile_router.register(
    r'profile',
    UserProfileViewSet,
    basename='profile'
)

urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(assignments_router.urls)),
    path(r'', include(profile_router.urls)),
    path('login', CustomAuthToken.as_view()),
    # path('authorize', CustomAuthToken.as_view()),
]
