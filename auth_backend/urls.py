from django.urls import include, path
from auth_backend.views import RegisterView

urlpatterns = [
    path("", include("rest_framework.urls")),
    path("register/", RegisterView.as_view(), name="auth_register"),
]
