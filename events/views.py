from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, BasePermission
from .models import Event
from .serializers import EventSerializer

# Create your views here.


class IsPassedUser(BasePermission):
    def has_permission(self, request, view):
        # Allow read access to users who have passed
        return request.user.passed


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('-id')
    # Admins can create, all passed users can read
    permission_classes = [IsAdminUser | IsPassedUser]

    def perform_create(self, serializer):
        # Ensure that the user who creates the event is an admin
        if self.request.user.is_superuser:
            serializer.save()
        else:
            raise PermissionDenied("Only admins can create events")
