from django.urls import include, path
from auth_backend.views import RegisterView, UserDetail, UserList

urlpatterns = [
    path("", include("rest_framework.urls")),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("users/", UserList.as_view()),
    path("users/<int:pk>", UserDetail.as_view()),
]
