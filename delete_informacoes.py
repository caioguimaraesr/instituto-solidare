import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from usuario.models import InformacoesPessoais

def delete_all_appointments():
    InformacoesPessoais.objects.all().delete()

if __name__ == "__main__":
    delete_all_appointments()