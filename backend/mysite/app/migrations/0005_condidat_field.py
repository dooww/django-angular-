# Generated by Django 3.0.3 on 2020-09-12 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_condidat_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='condidat',
            name='field',
            field=models.CharField(choices=[('confirmed', 'refused')], default='waiting', max_length=10),
        ),
    ]
