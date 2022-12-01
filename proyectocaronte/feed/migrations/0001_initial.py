# Generated by Django 4.1 on 2022-08-31 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=200)),
                ('adress', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('type_of_item', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('reference_number', models.IntegerField(default=666)),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200, unique=True)),
                ('accesories', models.CharField(max_length=200)),
                ('failure', models.TextField()),
                ('is_working', models.BooleanField()),
                ('is_damaged', models.BooleanField()),
                ('is_complete', models.BooleanField()),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('service_type', models.CharField(max_length=200)),
                ('client_pass', models.CharField(max_length=200, unique=True)),
                ('type_of_product', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.client')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('passwd', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='feed.service')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.user'),
        ),
        migrations.CreateModel(
            name='ItemDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=200, unique=True)),
                ('reference', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='feed.item')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='feed.service')),
            ],
        ),
        migrations.CreateModel(
            name='ClientComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='created')),
                ('updated_at', models.DateTimeField(verbose_name='updated')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='feed.client')),
            ],
        ),
    ]
