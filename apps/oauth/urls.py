from django.urls import path, include

from .views import GithubLoginView

urlpatterns = [
    path('', GithubLoginView.as_view())
]
