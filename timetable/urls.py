from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_view, name='timetable'),
    path('add/', views.add_slot, name='add_slot'),
    path('edit/<int:pk>/', views.update_slot, name='update_slot'),
    path('delete/<int:pk>/', views.delete_slot, name='delete_slot'),
]