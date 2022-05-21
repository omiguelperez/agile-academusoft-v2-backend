# Generated by Django 3.1.13 on 2021-10-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211001_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='doc_type',
            field=models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CC', 'Tarjeta de Identidad'), ('CC', 'Cédula de Extranjería')], default='TI', max_length=5),
        ),
        migrations.AddField(
            model_name='teacher',
            name='doc_type',
            field=models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CC', 'Tarjeta de Identidad'), ('CC', 'Cédula de Extranjería')], default='TI', max_length=5),
        ),
    ]
