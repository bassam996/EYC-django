# Generated by Django 3.2.8 on 2022-01-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carriers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='environment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/environment'),
        ),
        migrations.AddField(
            model_name='human_rights',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/human_rights'),
        ),
        migrations.AddField(
            model_name='peace',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/peace'),
        ),
        migrations.AddField(
            model_name='political_participation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/political_participation'),
        ),
        migrations.AddField(
            model_name='women',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/women'),
        ),
    ]