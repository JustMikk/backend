from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersGet, UsersNotPassedGet

router = DefaultRouter()
router.register('users', UsersGet, basename='users-get')
router.register('users-not-passed', UsersNotPassedGet,
                basename='users-not-passed-get')

urlpatterns = [
    path('', include(router.urls)),
]
