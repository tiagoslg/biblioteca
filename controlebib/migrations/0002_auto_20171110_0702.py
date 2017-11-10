# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlebib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEmprestimo', models.DateTimeField()),
                ('dataPrevDevolucao', models.DateTimeField()),
                ('dataDevolucao', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('autor', models.CharField(blank=True, max_length=200)),
                ('editora', models.CharField(blank=True, max_length=200)),
                ('status', models.IntegerField(choices=[('1', 'Disponível'), ('2', 'Emprestado')], default='1')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlebib.Livro'),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlebib.Usuario'),
        ),
    ]