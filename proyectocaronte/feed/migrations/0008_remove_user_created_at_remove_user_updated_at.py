# Generated by Django 4.1 on 2022-09-09 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_alter_user_created_at_alter_user_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]
