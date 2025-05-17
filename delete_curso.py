import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from instsoli.models import Curso

def delete_all_appointments():
    Curso.objects.all().delete()

if __name__ == "__main__":
    delete_all_appointments()