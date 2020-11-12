from django.urls import path

from . import views

urlpatterns = [
    path('account/<int:pk>/', views.ProfileView.as_view()),
    path('create_account/', views.CreateProfileView.as_view()),
]