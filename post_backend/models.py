from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        "auth.User", related_name="posts", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created_at"]
