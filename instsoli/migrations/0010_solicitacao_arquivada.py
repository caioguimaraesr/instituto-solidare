# Generated by Django 5.2 on 2025-05-18 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instsoli', '0009_solicitacao_solucao_resposta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='arquivada',
            field=models.BooleanField(default=False),
        ),
    ]
