# Generated by Django 4.2.2 on 2023-09-08 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_advance'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='page',
            name='type',
        ),
        migrations.AddField(
            model_name='page',
            name='id_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='principal.typepage'),
        ),
    ]
