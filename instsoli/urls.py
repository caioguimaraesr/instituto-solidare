from django.urls import path
from . import views

app_name = 'instsoli'

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/<int:id>/', views.detalhe_curso, name='detalhe_curso'),
    path('portal_professor/', views.portal_professor,name='portal_professor'),
    path('portal_professor/turmas/', views.gerenciar_turmas,name='gerenciar_turmas'),
    path('portal_professor/turmas/criar/', views.criar_turma,name='criar_turma'),
    path('turmas/excluir/<int:id>/', views.excluir_turma, name='excluir_turma'),
    path('turmas/editar/<int:id>/', views.editar_turma, name='editar_turma'),
]
