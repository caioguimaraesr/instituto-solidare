from django.urls import path
from . import views

app_name = 'instsoli'

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/<int:id>/', views.detalhe_curso, name='detalhe_curso'),
    path('portal_professor/', views.portal_professor,name='portal_professor'),
    path('portal_professor/turmas/', views.gerenciar_turmas,name='gerenciar_turmas'),
    
]
