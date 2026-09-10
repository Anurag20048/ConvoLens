from django.contrib import admin
from django.urls import include, path

from feedbackapp.health import health_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_view, name="health"),
    path("", include("feedbackapp.urls")),
]
