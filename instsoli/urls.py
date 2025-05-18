from django.urls import path
from . import views

app_name = 'instsoli'

urlpatterns = [
    path('', views.home, name='home'),
    # cursos
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/<int:id>/', views.detalhe_curso, name='detalhe_curso'),
    path('cursos/criar/', views.criar_curso, name='criar_curso'),
    path('cursos/gerenciar_cursos/', views.gerenciar_cursos ,name="gerenciar_cursos"),
    path('cursos/excluir/<int:id>', views.excluir_curso, name='excluir_curso'),
    path('cursos/editar/<int:id>', views.editar_curso, name='editar_curso'),

    ## portal do professor
    path('portal_professor/', views.portal_professor, name='portal_professor'),

    # turmas 
    path('portal_professor/turmas/', views.gerenciar_turmas, name='gerenciar_turmas'),
    path('portal_professor/turmas/criar/', views.criar_turma, name='criar_turma'),
    path('portal_professor/turmas/excluir/<int:id>/', views.excluir_turma, name='excluir_turma'),
    path('portal_professor/turmas/editar/<int:id>/', views.editar_turma, name='editar_turma'),
    path('portal_professor/turmas/alunos/<int:id>/', views.ver_alunos, name='ver_alunos'),
    path('portal_professor/turmas/frequencia/<int:id>', views.registrar_frequencia, name='registrar_frequencia'),

    # avisos
    path('portal_professor/avisos/', views.avisos, name='avisos'),
    path('portal_professor/avisos/criar/', views.criar_aviso, name='criar_aviso'),
    path('portal_professor/avisos/editar/<int:aviso_id>/', views.editar_aviso, name='editar_aviso'),
    path('portal_professor/avisos/excluir/<int:aviso_id>/', views.excluir_aviso, name='excluir_aviso'),
    path('portal_professor/avisos/get/<int:aviso_id>/', views.get_aviso_data, name='get_aviso_data'),

    ## solicitacoes professor
    path('portal_professor/solicitacoes/', views.professor_solicitacoes, name='professor_solicitacoes'),
    path('portal_professor/atualizar_solicitacao/<int:id>/', views.atualizar_solicitacao, name='atualizar_solicitacao'),
    path('portal_professor/capturar_solicitacao/<int:id>/', views.capturar_solicitacao, name='capturar_solicitacao'),

    ## portal do aluno
    path('portal_aluno/', views.portal_aluno, name='portal_aluno'),
    path('portal_aluno/avisos_aluno/', views.avisos_aluno, name='avisos_aluno'),

    # solicitacoes
    path('portal_aluno/listar_solicitacoes', views.list_solicitacoes, name='listar_solicitacoes'),
    path('portal_aluno/criar_solicitacoes/', views.create_solicitacao, name='criar_solicitacoes'),
    path('portal_aluno/editar_solicitacoes/<int:pk>/', views.edit_solicitacao, name='editar_solicitacoes'),
    path('portal_aluno/deletar_solicitacoes/<int:pk>/', views.delete_solicitacao, name='deletar_solicitacoes'),
    
]
