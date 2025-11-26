
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='create'),
    path('read/', views.read_student, name='read'),
    path('update/<int:pk>/', views.update_student, name='update'),
    path('delete/<int:pk>/', views.delete_student, name='delete'),
]
