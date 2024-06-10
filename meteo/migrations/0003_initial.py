# Generated by Django 4.0.6 on 2024-06-06 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meteo', '0002_delete_previsaotempo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Previsao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
                ('descricao_tempo', models.CharField(max_length=255)),
                ('precipitacao', models.FloatField()),
                ('icone_url', models.URLField()),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteo.cidade')),
            ],
        ),
    ]