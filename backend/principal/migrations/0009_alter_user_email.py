# Generated by Django 4.2.2 on 2023-11-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_earning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]