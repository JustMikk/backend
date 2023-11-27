from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, AnnouncementViewSet, SuperUserCheckView, TotalMember, TotalNewMember

router = DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register('announcements', AnnouncementViewSet, basename='announcement')

urlpatterns = [
    path('', include(router.urls)),
    path("is_admin/", SuperUserCheckView.as_view()),
    path("newmembers/", TotalNewMember.as_view()),
    path("members/", TotalMember.as_view()),
]
