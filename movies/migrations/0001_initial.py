# Generated by Django 5.0.3 on 2024-05-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_initial'),
        ('credits', '0001_initial'),
        ('genders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField(default=False)),
                ('backdrop_path', models.CharField(blank=True, max_length=255, null=True)),
                ('belongs_to_collection', models.CharField(blank=True, max_length=255, null=True)),
                ('budget', models.FloatField(blank=True, null=True)),
                ('homepage', models.URLField(blank=True, null=True)),
                ('original_language', models.CharField(max_length=20, null=True)),
                ('original_title', models.CharField(default='', max_length=255)),
                ('overview', models.TextField(blank=True, null=True)),
                ('poster_path', models.CharField(default='', max_length=255)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('revenue', models.FloatField(blank=True, null=True)),
                ('runtime', models.FloatField(blank=True, null=True)),
                ('tagline', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('video', models.BooleanField(default=False)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('actor', models.ManyToManyField(blank=True, to='actors.actor')),
                ('genres', models.ManyToManyField(blank=True, to='genders.gender')),
                ('producer', models.ManyToManyField(blank=True, to='credits.productor')),
            ],
        ),
    ]
