# Generated by Django 3.1.7 on 2021-03-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210316_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]