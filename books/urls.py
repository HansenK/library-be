from django.urls import path

from . import views

urlpatterns = [
  path('', views.BooksList.as_view(), name="list"),
  path('<int:id>/', views.BookDetail.as_view(), name="book"),

  path('tags', views.TagsList.as_view(), name="tags")
]