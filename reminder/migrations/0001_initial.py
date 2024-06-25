# Generated by Django 4.2.11 on 2024-06-25 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=11, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('notification_time', models.DateField(null=True)),
                ('message', models.TextField(null=True)),
                ('send_message_time', models.DateField(null=True)),
                ('congrats_birth', models.BooleanField(null=True)),
                ('congrats_birth_message', models.TextField(null=True)),
                ('send_type', models.CharField(choices=[('EM', 'Email'), ('PN', 'Phone number'), ('BO', 'Both'), ('NO', 'None')], default='NO', max_length=3)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('person_profile_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massage', models.TextField()),
                ('send_massage_time', models.DateTimeField()),
                ('send_type', models.CharField(choices=[('EM', 'Email'), ('PN', 'Phone number'), ('BO', 'Both'), ('NO', 'None')], default='NO', max_length=3)),
                ('person_profile_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
                ('persons_rel', models.ManyToManyField(to='reminder.person')),
            ],
        ),
    ]
