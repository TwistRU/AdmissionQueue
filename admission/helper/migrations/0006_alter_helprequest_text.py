# Generated by Django 5.0.4 on 2024-06-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0005_helprequest_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helprequest',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
