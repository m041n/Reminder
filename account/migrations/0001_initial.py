# Generated by Django 4.2.11 on 2024-06-24 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('SU', 'Suspend'), ('AC', 'Active'), ('DE', 'Delete'), ('CL', 'Close'), ('BA', 'Banned')], default='AC', max_length=3)),
                ('account_type', models.CharField(choices=[('SU', 'Superuser user'), ('AD', 'Admin user'), ('CU', 'Customer user')], default='CU', max_length=3)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('SU', 'Suspend'), ('AC', 'Accepted'), ('BA', 'Banned')], default='SU', max_length=3)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('national_id', models.CharField(max_length=10, unique=True)),
                ('image', models.ImageField(upload_to='account/face_image/')),
                ('birth_date', models.DateField()),
                ('token', models.CharField(max_length=255)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_rel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
