# Generated by Django 4.2.11 on 2024-06-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='token',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
