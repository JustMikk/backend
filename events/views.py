from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, request
from rest_framework.permissions import IsAdminUser, BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event, Announcement
from .serializers import EventSerializer, AnnouncementSerializer


class SuperUserCheckView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        is_superuser = (
            request.user.is_authenticated and request.user.is_superuser
        )
        return Response({'is_superuser': is_superuser})


class TotalMember(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        User = get_user_model()
        total = User.objects.all().filter(passed=True).count()
        return Response({'total': total})


class TotalNewMember(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        User = get_user_model()
        total = User.objects.all().filter(passed=False).count()
        return Response({'total': total})


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


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all().order_by('-id')

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()
        else:
            raise PermissionDenied("Only admins can create announcements")

    def perform_destroy(self, instance):
        if self.request.user.is_superuser:
            instance.delete()
        else:
            raise PermissionDenied("Only admins can delete announcements")

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()
        else:
            raise PermissionDenied("Only admins can update announcements")
