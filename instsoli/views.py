from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso,Turma, Frequencia, Aviso
from usuario.models import InformacoesPessoais
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
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
@user_passes_test(is_admin)
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

def avisos(request):
    avisos = Aviso.objects.filter(professor=request.user).order_by('-data_criacao')
    return render(request, 'instsoli/pages/portal_professor/avisos/avisos.html', context={
        'avisos': avisos
    })

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

@login_required
def get_aviso_data(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id, professor=request.user)
    data = {
        'titulo': aviso.titulo,
        'mensagem': aviso.mensagem,
        'prioridade': aviso.prioridade,
    }
    return JsonResponse(data)

@login_required
def excluir_aviso(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id, professor=request.user)
    aviso.delete()
    return redirect('instsoli:avisos')

### portal do aluno
def portal_aluno(request):
    return render(request, 'instsoli/pages/portal_aluno/portal_aluno.html')

def avisos_aluno(request):
    avisos = Aviso.objects.all().order_by('-data_criacao')
    return render(request, 'instsoli/pages/portal_aluno/avisos/avisos_aluno.html', context={
        'avisos': avisos
    })