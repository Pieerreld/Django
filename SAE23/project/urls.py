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
    path('machine_add',
        views.machine_add_form,
        name='machine_add'),
]