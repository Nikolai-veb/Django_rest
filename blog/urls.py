from django.urls import path
from . import views


urlpatterns = [
        path("article/", views.ArticleView.as_view()),
        path("article/<int:pk>/", views.ArticleDetailView.as_view()),
        path("tags/", views.TagView.as_view()),
]