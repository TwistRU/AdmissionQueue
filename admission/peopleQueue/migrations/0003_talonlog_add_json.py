# Generated by Django 5.0 on 2024-04-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleQueue', '0002_talon_purpose'),
    ]

    operations = [
        migrations.AddField(
            model_name='talonlog',
            name='add_json',
            field=models.JSONField(default=dict),
        ),
    ]
