# Generated by Django 4.1 on 2022-09-07 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_typeofitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type_of_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='feed.typeofitem'),
        ),
    ]
