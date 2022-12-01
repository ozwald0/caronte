# Generated by Django 4.1 on 2022-09-20 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_remove_user_created_at_remove_user_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='level',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='statusofusers',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='statusofusers',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='statusofusers',
            name='name',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='feed.level'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='feed.statusofusers'),
        ),
    ]
