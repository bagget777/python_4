
from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.get_contacts, name='contacts'),
    path('about/', views.get_about, name='about'),
    path('test/<str:string>', views.catch_string, name='catch-string'),
]
