from django.urls import path, include

from .views import GithubCodeView

urlpatterns = [
    path('', GithubCodeView.as_view())
]
