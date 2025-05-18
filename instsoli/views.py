from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso,Turma, Frequencia, Aviso, Solicitacao
from usuario.models import InformacoesPessoais
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import date

def is_admin(user):
    if not user.is_superuser:
        return False 
    return True

def home(request):
    return render(request, 'instsoli/pages/home.html')

# cursos
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'instsoli/pages/cursos/cursos.html', context={
        'cursos':cursos
    })

def detalhe_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'instsoli/pages/cursos/cursos_detalhes.html', context={
        'curso': curso
    })

@login_required(login_url='usuario:login')
@user_passes_test(is_admin)
def criar_curso(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('desc')
        imagem = request.FILES.get('imagem')
        grade = request.FILES.get('grade')

        Curso.objects.create(
            nome=nome,
            descricao=descricao,
            imagem=imagem,
            documento=grade,
        )

        return redirect('instsoli:cursos')

    return render(request, 'instsoli/pages/cursos/criar_curso.html')

def gerenciar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'instsoli/pages/cursos/gerenciar_cursos.html', context={
        'cursos':cursos
    })

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("desc")
        imagem = request.FILES.get("imagem")
        grade = request.FILES.get("grade")

        curso.nome = nome
        curso.descricao = descricao

        if imagem:
            curso.imagem = imagem

        if grade:
            curso.grade = grade

        curso.save()
        return redirect('instsoli:gerenciar_cursos') 
    return render(request, 'instsoli/pages/cursos/editar_curso.html', context={
        "curso": curso
        })

def excluir_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    messages.success(request, 'Curso excluída com sucesso!')
    return redirect('instsoli:gerenciar_cursos')

### portal do professor
@login_required(login_url='usuario:login')
@user_passes_test(is_admin, login_url='instsoli:home')
def portal_professor(request):
    return render(request, 'instsoli/pages/portal_professor/portal_professor.html')

# turmas 
@login_required(login_url='usuario:login')
@user_passes_test(is_admin, login_url='instsoli:home')
def gerenciar_turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'instsoli/pages/portal_professor/turmas/gerenciar_turmas.html', context={
        'turmas':turmas
    })

@login_required(login_url='usuario:login')
@user_passes_test(is_admin, login_url='instsoli:home')
def criar_turma(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        curso_id = request.POST.get('curso')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        alunos_ids = request.POST.getlist('alunos')

        curso = Curso.objects.get(id=curso_id)
        turma = Turma.objects.create(
            nome=nome,
            curso=curso,
            data_inicio=data_inicio,
            data_fim=data_fim
        )

        if alunos_ids:
            turma.alunos.set(alunos_ids)

        return redirect('instsoli:gerenciar_turmas')

    cursos = Curso.objects.all()
    alunos = InformacoesPessoais.objects.all()

    return render(request, 'instsoli/pages/portal_professor/turmas/criar_turma.html', {
        'cursos': cursos,
        'alunos': alunos,
    })

@login_required(login_url='usuario:login')
@user_passes_test(is_admin, login_url='instsoli:home')
def editar_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    cursos = Curso.objects.all()
    alunos = InformacoesPessoais.objects.all()

    if request.method == 'POST':
        turma.nome = request.POST.get('nome')
        turma.curso_id = request.POST.get('curso')
        turma.data_inicio = request.POST.get('data_inicio')
        turma.data_fim = request.POST.get('data_fim')
        
        turma.save()

        alunos_ids = request.POST.getlist('alunos')
        turma.alunos.set(alunos_ids)

        return redirect('instsoli:gerenciar_turmas')

    return render(request, 'instsoli/pages/portal_professor/turmas/editar_turma.html', context={
        'turma': turma,
        'cursos': cursos,
        'alunos': alunos,
    })

@login_required(login_url='usuario:login')
@user_passes_test(is_admin, login_url='instsoli:home')
def excluir_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    turma.delete()
    messages.success(request, 'Turma excluída com sucesso!')
    return redirect('instsoli:gerenciar_turmas')

def ver_alunos(request, id):
    turma = get_object_or_404(Turma, id=id)
    alunos = turma.alunos.all()
    return render(request, 'instsoli/pages/portal_professor/turmas/ver_alunos.html', context={
        'turma':turma,
        'alunos':alunos,
    })

def registrar_frequencia(request, id):
    turma = get_object_or_404(Turma, id=id)
    alunos = turma.alunos.all()
    
    data_selecionada = request.POST.get('data') or request.GET.get('data') or date.today().isoformat()
    
    if request.method == 'POST':
        if 'salvar' in request.POST:
            data = request.POST.get('data')
            for aluno in alunos:
                presente = request.POST.get(f'presente_{aluno.id}') == 'on'
                Frequencia.objects.update_or_create(
                    turma=turma,
                    aluno=aluno,
                    data=data,
                    defaults={'presente': presente}
                )
            messages.success(request, 'Frequência salva com sucesso!')
            return redirect('instsoli:registrar_frequencia', id=turma.id)
        
        elif 'buscar' in request.POST:
            pass  

    frequencias = Frequencia.objects.filter(
        turma=turma,
        data=data_selecionada
    ).select_related('aluno')

    alunos_presentes = [freq.aluno.id for freq in frequencias if freq.presente]
    alunos_ausentes = [freq.aluno.id for freq in frequencias if not freq.presente]

    return render(request, 'instsoli/pages/portal_professor/turmas/registrar_frequencia.html', context = {
        'turma': turma,
        'alunos': alunos,
        'data_selecionada': data_selecionada,
        'alunos_presentes': alunos_presentes,
        'alunos_ausentes': alunos_ausentes,
    })

# avisos professor
@user_passes_test(is_admin, login_url='instsoli:home')
@login_required(login_url='usuario:login')
def avisos(request):
    avisos = Aviso.objects.filter(professor=request.user).order_by('-data_criacao')
    return render(request, 'instsoli/pages/portal_professor/avisos/avisos.html', context={
        'avisos': avisos
    })

@user_passes_test(is_admin, login_url='instsoli:home')
@login_required(login_url='usuario:login')
def criar_aviso(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        mensagem = request.POST.get('mensagem')
        prioridade = request.POST.get('prioridade')

        Aviso.objects.create(
            professor=request.user,
            titulo=titulo,
            mensagem=mensagem,
            prioridade=prioridade
        )
        return redirect('instsoli:avisos')

@user_passes_test(is_admin, login_url='instsoli:home')
@login_required(login_url='usuario:login')
def editar_aviso(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id, professor=request.user)

    if request.method == 'POST':
        aviso.titulo = request.POST.get('titulo')
        aviso.mensagem = request.POST.get('mensagem')
        aviso.prioridade = request.POST.get('prioridade')
        aviso.save()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        
        return redirect('instsoli:avisos')

    return render(request, 'editar_aviso.html', {'aviso': aviso})

@user_passes_test(is_admin, login_url='instsoli:home')
@login_required(login_url='usuario:login')
def get_aviso_data(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id, professor=request.user)
    data = {
        'titulo': aviso.titulo,
        'mensagem': aviso.mensagem,
        'prioridade': aviso.prioridade,
    }
    return JsonResponse(data)

@user_passes_test(is_admin, login_url='instsoli:home')
@login_required(login_url='usuario:login')
def excluir_aviso(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id, professor=request.user)
    aviso.delete()
    return redirect('instsoli:avisos')

# solicitacoes professor
@user_passes_test(is_admin, login_url='instsoli:home')
@login_required(login_url='usuario:login')
def professor_solicitacoes(request):
    solicitacoes = Solicitacao.objects.filter(arquivada=False)
    return render(request, 'instsoli/pages/portal_professor/solicitacoes/solicitacoes_professor.html', {
        'solicitacoes': solicitacoes
    })

@user_passes_test(is_admin, login_url='instsoli:home')
@login_required(login_url='usuario:login')
def arquivar_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    if request.method == 'POST':
        solicitacao.arquivar()
        return JsonResponse({
            'success': True,
            'message': 'Solicitação arquivada com sucesso!'
        })
    
    return JsonResponse({
        'success': False,
        'message': 'Método não permitido'
    }, status=400)

@user_passes_test(is_admin, login_url='instsoli:home')
@login_required(login_url='usuario:login')
def atualizar_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    
    if request.method == 'POST':
        novo_status = request.POST.get('status')
        resposta = request.POST.get('solucao_resposta')

        solicitacao.status = novo_status
        solicitacao.solucao_resposta = resposta
        solicitacao.professor = request.user
        solicitacao.save()

        return redirect('instsoli:professor_solicitacoes')
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'id': solicitacao.id,
            'status': solicitacao.status,
            'solucao_resposta': solicitacao.solucao_resposta,
            'titulo': solicitacao.titulo,
            'mensagem': solicitacao.mensagem,
            'tipo': solicitacao.tipo,
            'aluno': solicitacao.aluno.username,
            'data': solicitacao.data_criacao.strftime('%d/%m/%Y %H:%M')
        })

    return redirect('instsoli:professor_solicitacoes')

@user_passes_test(is_admin, login_url='instsoli:home')
@login_required(login_url='usuario:login')
def capturar_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    
    if request.method == 'POST':
        if solicitacao.status == 'pendente':
            solicitacao.status = 'em_andamento'
            solicitacao.professor = request.user
            solicitacao.save()
            
            return JsonResponse({
                'success': True,
                'message': 'Solicitação capturada com sucesso!'
            })
        else:
            if solicitacao.professor and solicitacao.professor != request.user:
                return JsonResponse({
                    'success': False,
                    'message': f'Esta solicitação já está sendo tratada pelo professor {solicitacao.professor.get_full_name()}'
                }, status=400)
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Esta solicitação já está em andamento'
                }, status=400)

    return redirect('instsoli:professor_solicitacoes')

### portal do aluno
@login_required(login_url='usuario:login')
def portal_aluno(request):
    return render(request, 'instsoli/pages/portal_aluno/portal_aluno.html')

# avisos aluno
@login_required(login_url='usuario:login')
def avisos_aluno(request):
    avisos = Aviso.objects.all().order_by('-data_criacao')
    return render(request, 'instsoli/pages/portal_aluno/avisos/avisos_aluno.html', context={
        'avisos': avisos
    })

# solicitacoes aluno
@login_required(login_url='usuario:login')
def list_solicitacoes(request):
    solicitacoes = Solicitacao.objects.filter(aluno=request.user)
    return render(request, 'instsoli/pages/portal_aluno/solicitacoes/minhas_solicitacoes.html', context={
        'solicitacoes': solicitacoes
    })

@login_required(login_url='usuario:login')
def create_solicitacao(request):
    titulo = request.POST.get('titulo')
    mensagem = request.POST.get('mensagem')
    tipo = request.POST.get('tipo')

    Solicitacao.objects.create(
        titulo=titulo,
        mensagem=mensagem,
        tipo=tipo,
        aluno=request.user,
    )
    return redirect('instsoli:listar_solicitacoes')


@login_required(login_url='usuario:login')
def edit_solicitacao(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)

    if request.method == 'GET':
        return JsonResponse({
            'titulo': solicitacao.titulo,
            'mensagem': solicitacao.mensagem,
            'tipo': solicitacao.tipo,
            'status': None,
        })

    elif request.method == 'POST':
        solicitacao.titulo = request.POST.get('titulo')
        solicitacao.mensagem = request.POST.get('mensagem')
        solicitacao.tipo = request.POST.get('tipo')
        solicitacao.save()
        return redirect('instsoli:listar_solicitacoes')


@login_required(login_url='usuario:login')
def delete_solicitacao(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)

    solicitacao.delete()
    return redirect('instsoli:listar_solicitacoes')