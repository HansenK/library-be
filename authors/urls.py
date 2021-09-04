from django.urls import path

from . import views

urlpatterns = [
  path('', views.AuthorsList.as_view(), name="list"),
]