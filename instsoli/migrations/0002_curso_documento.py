# Generated by Django 5.1.6 on 2025-04-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instsoli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='documentos_cursos/'),
        ),
    ]
