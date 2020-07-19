from django.urls import path, include
from rest_framework_nested import routers

from .views import (
    UserViewSet, AssignmentViewSet, CustomAuthToken, UserProfileViewSet
)

router = routers.SimpleRouter()
router.register(r'', UserViewSet)

assignments_router = routers.NestedSimpleRouter(router, r'', lookup='list')
assignments_router.register(r'assignments', AssignmentViewSet)

profile_router = routers.NestedSimpleRouter(router, r'', lookup='profile')
profile_router.register(r'profile', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(assignments_router.urls)),
    path(r'', include(profile_router.urls)),
    path('login', CustomAuthToken.as_view()),
    # path('authorize', CustomAuthToken.as_view()),
]
