# Generated by Django 5.0.3 on 2024-05-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0001_initial'),
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='producer',
            field=models.ManyToManyField(blank=True, to='credits.productor'),
        ),
    ]
