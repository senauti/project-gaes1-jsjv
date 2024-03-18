# Generated by Django 4.2.7 on 2024-03-17 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(choices=[('8 Horas', '8 Horas'), ('5 Horas', '5 Horas'), ('6 Horas', '6 Horas')], max_length=255, verbose_name='Horario del empleado')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
                'db_table': 'horario',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailSalary', models.CharField(blank=True, max_length=100, null=True, verbose_name='Detalle salario')),
                ('numberAccount', models.BigIntegerField(null=True, verbose_name='Numero de Cuenta')),
                ('amountActivity', models.IntegerField(null=True, verbose_name='Cantidad de Actividad')),
                ('totalSalary', models.FloatField(blank=True, null=True, verbose_name='Total salario')),
                ('Activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Activity_ActivityValue', to='actividades.activity', verbose_name='Actividad')),
                ('nameEmploye', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name_employe', to=settings.AUTH_USER_MODEL, verbose_name='Nombre del Empleado')),
                ('schedules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionHumana.schedule', verbose_name='Ingreso de Empleado')),
            ],
            options={
                'verbose_name': 'Salario',
                'verbose_name_plural': 'Salarios',
                'db_table': 'sueldo',
                'ordering': ['id'],
            },
        ),
    ]