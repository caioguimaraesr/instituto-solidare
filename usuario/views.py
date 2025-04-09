from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'usuario/pages/login.html')

def register(request):
    return render(request, 'usuario/pages/register.html')