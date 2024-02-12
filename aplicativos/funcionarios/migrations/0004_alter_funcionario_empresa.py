# Generated by Django 3.2.23 on 2024-02-05 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('funcionarios', '0003_alter_funcionario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresas'),
        ),
    ]
