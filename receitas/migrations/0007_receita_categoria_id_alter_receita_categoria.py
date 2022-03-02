# Generated by Django 4.0.2 on 2022-02-20 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0006_categoria_alter_receita_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='categoria_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receitas.categoria'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='categoria',
            field=models.CharField(max_length=100),
        ),
    ]