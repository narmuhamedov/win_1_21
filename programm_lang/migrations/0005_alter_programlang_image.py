# Generated by Django 4.2.6 on 2023-10-28 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programm_lang', '0004_reviewproglang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programlang',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]