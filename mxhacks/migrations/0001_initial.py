# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=1000)),
                ('law', models.CharField(max_length=1000)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.CharField(max_length=1000)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mxhacks.City')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=1000)),
                ('reference', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=1000)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mxhacks.City')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('img', models.CharField(default=' ', max_length=100)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='procedure',
            name='tags',
            field=models.ManyToManyField(to='mxhacks.Tags'),
        ),
        migrations.AddField(
            model_name='law',
            name='tags',
            field=models.ManyToManyField(to='mxhacks.Tags'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mxhacks.Country'),
        ),
    ]
