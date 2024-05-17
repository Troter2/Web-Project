# Generated by Django 5.0.3 on 2024-05-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('biography', models.TextField(default='', max_length=5000)),
                ('also_known_as', models.TextField(default='', max_length=5000)),
                ('gender', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
