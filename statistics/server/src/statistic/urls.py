from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/likes/",include("likes.urls")),
    path("api/auth/",include("members.urls")),
    path("api/users/",include("users.urls")),
    path("api/vacations/",include("vacations.urls")),
]
