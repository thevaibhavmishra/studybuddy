from django.contrib import admin
from django.urls import path
from .views import home, room, createRoom, updateRoom, deleteRoom, loginView, logoutView, registerView, deleteMessage, userProfile

urlpatterns = [
    path("", home, name="home" ),
    path("login/", loginView, name="login" ),
    path("register/", registerView, name="register" ),
    path("logout/", logoutView, name="logout" ),
    path("profile/<str:pk>", userProfile, name="profile" ),
    path("create-room/", createRoom, name="create-room"),
    path("room/<str:pk>", room, name="room" ),
    path("update-room/<str:pk>", updateRoom, name="update-room" ),
    path("delete-room/<str:pk>", deleteRoom, name="delete-room" ),
    path("delete-message/<str:pk>", deleteMessage, name="delete-message" ),
]
