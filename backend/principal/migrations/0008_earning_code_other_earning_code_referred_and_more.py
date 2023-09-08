# Generated by Django 4.2.2 on 2023-09-08 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_account_code_studio_account_percentage_studio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='earning',
            name='code_other',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='other_earning', to='principal.user'),
        ),
        migrations.AddField(
            model_name='earning',
            name='code_referred',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referred_earning', to='principal.user'),
        ),
        migrations.AddField(
            model_name='earning',
            name='code_studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='studio_earning', to='principal.user'),
        ),
        migrations.AddField(
            model_name='earning',
            name='code_substudio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='substudio_earning', to='principal.user'),
        ),
        migrations.AddField(
            model_name='earning',
            name='code_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_earning', to='principal.user'),
        ),
        migrations.AddField(
            model_name='earning',
            name='percentage_other',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='earning',
            name='percentage_referred',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='earning',
            name='percentage_studio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='earning',
            name='percentage_substudio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='earning',
            name='percentage_user',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
