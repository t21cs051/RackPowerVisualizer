# Generated by Django 4.1 on 2024-01-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_alter_ups_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ups',
            name='description',
            field=models.TextField(default=''),
        ),
    ]