# Generated by Django 5.0.3 on 2024-03-27 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='test',
            new_name='idProduction',
        ),
    ]