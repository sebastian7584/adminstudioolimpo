# Generated by Django 4.2.2 on 2023-09-08 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_typepage_remove_page_type_page_id_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='principal.owner'),
        ),
    ]
