# Generated by Django 2.0.9 on 2018-11-12 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('Address_id', models.AutoField(primary_key=True, serialize=False)),
                ('home', models.CharField(max_length=50)),
                ('society', models.CharField(max_length=300)),
                ('Area', models.CharField(choices=[('thames', 'thames'), ('lambeth', 'lambeth'), ('southpark', 'southpark'), ('nova', 'nova')], max_length=60)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=60)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('Customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('mobilenumber', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
