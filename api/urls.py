from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.shortcuts import render


def render_react(request):
    return render(request, "index.html")


urlpatterns = [
    path('superuser/', admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('api/', include('accounts.urls')),
    path('api/', include('events.urls')),
    re_path(r"^$", render_react),
    re_path(r"^(?:.*)/?$", render_react),
]

# urlpatterns += [re_path(r'^.*',
# TemplateView.as_view(template_name='index.html'))]
