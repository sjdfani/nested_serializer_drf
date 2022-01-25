from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import get_user_model
from .serializer import UserSerializer


class UserList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
