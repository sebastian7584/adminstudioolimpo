# Generated by Django 4.2.2 on 2023-11-27 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(null=True),
        ),
    ]
