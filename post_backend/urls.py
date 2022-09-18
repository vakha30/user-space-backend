from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListCreatePostAPIView.as_view(), name="get_posts"),
    path(
        "<int:pk>/",
        views.RetrieveUpdateDestroyPostAPIView.as_view(),
        name="get_delete_update_post",
    ),
]
