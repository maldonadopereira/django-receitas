# Generated by Django 4.0.2 on 2022-02-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_alter_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicar',
            field=models.BooleanField(default=False),
        ),
    ]
