from django.urls import path
from . import views

urlpatterns = [
    path('kmexam/', views.kmexam_list, name='kmexam_list'),
]
