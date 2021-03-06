# Generated by Django 3.2.12 on 2022-03-20 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('data', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data')),
                ('_cache_qtde', models.IntegerField(editable=False, verbose_name='Qtde de casas')),
            ],
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
    ]
