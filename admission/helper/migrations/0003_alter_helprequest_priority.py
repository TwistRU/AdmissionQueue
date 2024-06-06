# Generated by Django 5.0.4 on 2024-06-05 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_helprequest_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helprequest',
            name='priority',
            field=models.CharField(choices=[('Low', 'Низкая'), ('Medium', 'Средняя'), ('High', 'Высокая')], max_length=6),
        ),
    ]
