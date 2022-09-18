from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/auth/", include("auth_backend.urls")),
    path("api/posts/", include("post_backend.urls")),
    path("admin/", admin.site.urls),
]
