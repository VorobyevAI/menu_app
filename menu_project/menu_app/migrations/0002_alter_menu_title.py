# Generated by Django 4.1.7 on 2023-02-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Menu title'),
        ),
    ]
