import os

import requests
from django.http import JsonResponse
from rest_framework import serializers, generics, permissions, status, views
from rest_framework.response import Response
from requests.exceptions import HTTPError
 
from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden


class GithubCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255, required=True)
    clientId = serializers.CharField(max_length=255)
    redirectUri = serializers.CharField(max_length=255)


class GithubCodeView(generics.GenericAPIView):
    serializer_class = GithubCodeSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        ACCESS_URL = 'https://github.com/login/oauth/access_token'

        payload = {
            'code': request.data['code'],
            'client_id': os.environ['GITHUB_CLIENT_ID'],
            'client_secret': os.environ['GITHUB_CLIENT_SECRET']
        }
        headers = {
            'Accept': 'application/json'
        }
        res = requests.post(ACCESS_URL, payload, headers=headers)
        print(res.text)
        return Response(res.text, status=200)
