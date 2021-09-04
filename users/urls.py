from django.urls import path

from . import views

urlpatterns = [
    path('', views.UsersList.as_view(), name='list'),
    path('<int:id>/', views.UserDetail.as_view(), name="user"),
]