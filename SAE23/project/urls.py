from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('liste_personnel/', views.liste_personnel, name='liste_personnel'),
    path('liste_machine/', views.liste_machine, name='liste_machine'),
    path('machine/<pk>',
         views.machine_view,
         name='machine_view'),
    path('personnel/<pk>',
         views.personnel_view,
         name='personnel_view'),
    path('ajout_machine_personnel/',
          views.add_machine_personnel, 
          name='ajout_machine_personnel'),
     path('supprimer_machine/<pk>',
          views.supprimer_machine,
          name='supprimer_machine'),
     path('supprimer_personnel/<pk>',
          views.supprimer_personnel,
          name='supprimer_personnel'),
     path('chatbot',
          views.chatbot,
          name='chatbot'),
]