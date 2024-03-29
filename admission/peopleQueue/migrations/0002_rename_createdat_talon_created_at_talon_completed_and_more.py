# Generated by Django 5.0 on 2024-02-29 02:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleQueue', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='talon',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='talon',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talon',
            name='completed_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='talon',
            name='completed_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='completed_talons', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='talon',
            name='compliting_by',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compliting_talon', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='talon',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='talons_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='talon',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='talon',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='talons_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
