# Generated by Django 4.0.2 on 2022-02-20 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0005_receita_foto_receita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='receita',
            name='categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receitas.categoria'),
        ),
    ]