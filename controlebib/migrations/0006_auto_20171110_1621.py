# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlebib', '0005_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='dataDevolucao',
            field=models.DateTimeField(null=True, verbose_name='Data de dataDevolucao'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataEmprestimo',
            field=models.DateTimeField(verbose_name='Data do Empréstimo'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataPrevDevolucao',
            field=models.DateTimeField(verbose_name='Data para Devolução'),
        ),
    ]
