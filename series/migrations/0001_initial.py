# Generated by Django 5.0.3 on 2024-05-14 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('credits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='seasonDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_date', models.DateField()),
                ('episodes', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('overview', models.TextField(blank=True, null=True)),
                ('poster_path', models.CharField(default='', max_length=255)),
                ('season_number', models.IntegerField()),
                ('vote_average', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='episodeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_date', models.DateField()),
                ('crew', models.CharField(max_length=255)),
                ('episode_number', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('overview', models.TextField(blank=True, null=True)),
                ('runtime', models.IntegerField()),
                ('still_path', models.CharField(default='', max_length=255)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.seasondetail')),
            ],
        ),
        migrations.CreateModel(
            name='serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serieName', models.CharField(default='noSerie', max_length=100)),
                ('overview', models.TextField(default='No overview')),
                ('number_of_episodes', models.IntegerField(default=0)),
                ('number_of_seasons', models.IntegerField(default=0)),
                ('in_production', models.BooleanField(default=False)),
                ('original_language', models.CharField(default='', max_length=100)),
                ('producer', models.ManyToManyField(blank=True, to='credits.productor')),
            ],
        ),
        migrations.AddField(
            model_name='seasondetail',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.serie'),
        ),
    ]
