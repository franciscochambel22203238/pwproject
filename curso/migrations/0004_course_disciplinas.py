# Generated by Django 4.0.6 on 2024-05-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_remove_project_discipline'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='disciplinas',
            field=models.ManyToManyField(related_name='courses', to='curso.discipline'),
        ),
    ]
