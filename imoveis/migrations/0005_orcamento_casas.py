# Generated by Django 3.2.12 on 2022-03-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0004_auto_20220319_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='casas',
            field=models.ManyToManyField(to='imoveis.Casa'),
        ),
    ]