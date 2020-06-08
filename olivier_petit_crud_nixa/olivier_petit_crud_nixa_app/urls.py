from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from olivier_petit_crud_nixa_app import views

urlpatterns = [
    path('olivier_petit_crud_nixa_app/', views.ClientList.as_view()),
    path('olivier_petit_crud_nixa_app/<int:pk>/', views.ClientDetail.as_view()),
]
