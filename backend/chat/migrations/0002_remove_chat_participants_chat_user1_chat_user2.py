# Generated by Django 5.0.4 on 2024-05-02 20:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='participants',
        ),
        migrations.AddField(
            model_name='chat',
            name='user1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chats_as_user1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='user2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chats_as_user2', to=settings.AUTH_USER_MODEL),
        ),
    ]
