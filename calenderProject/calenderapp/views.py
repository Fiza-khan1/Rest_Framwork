
from rest_framework import generics
from .models import CustomUser
from .sevilizer import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
