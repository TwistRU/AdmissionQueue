# Generated by Django 5.0.4 on 2024-05-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleQueue', '0005_alter_talonlog_action_delete_talonaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='talon',
            name='ordinal',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
