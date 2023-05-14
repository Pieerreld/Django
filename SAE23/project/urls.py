from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('liste_personnel/', views.liste_personnel, name='liste_personnel'),
]