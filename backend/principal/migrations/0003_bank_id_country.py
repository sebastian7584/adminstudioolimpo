# Generated by Django 4.2.2 on 2023-09-01 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_user_admin_alter_user_account_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='id_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='principal.country'),
        ),
    ]
