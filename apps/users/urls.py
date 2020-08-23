from django.urls import path, include
from rest_framework_nested import routers

from .views import (
    UserViewSet, SubmissionsViewSet, CustomAuthToken, UserProfileView
)

router = routers.SimpleRouter()
router.register(r'', UserViewSet)

assignments_router = routers.NestedSimpleRouter(router, r'', lookup='list')
assignments_router.register(
    r'submissions',
    SubmissionsViewSet,
    basename='submissions'
)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/profile/',
         UserProfileView.as_view(), name='user-profile'),
    path('', include(assignments_router.urls)),
    path('login', CustomAuthToken.as_view()),
    # path('authorize', CustomAuthToken.as_view()),
]
