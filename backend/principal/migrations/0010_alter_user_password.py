# Generated by Django 4.2.2 on 2023-11-27 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
