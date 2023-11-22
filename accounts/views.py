from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer
from .models import User

# Create your views here.


class UsersGet(ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(passed=True)


class UsersNotPassedGet(ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(passed=False)
