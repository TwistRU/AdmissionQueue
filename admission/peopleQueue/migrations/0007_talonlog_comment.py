# Generated by Django 5.0.4 on 2024-05-10 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleQueue', '0006_talon_ordinal'),
    ]

    operations = [
        migrations.AddField(
            model_name='talonlog',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
    ]
