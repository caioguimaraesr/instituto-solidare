# Generated by Django 5.2 on 2025-04-19 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instsoli', '0003_turma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='descricao',
        ),
    ]
