# Generated by Django 5.0.4 on 2024-05-01 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('taller', models.CharField(max_length=100)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('hora', models.TimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]