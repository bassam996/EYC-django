# Generated by Django 3.2.8 on 2022-01-08 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0014_auto_20220108_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='desc_job',
        ),
        migrations.AddField(
            model_name='board',
            name='job_title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='job_title_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='name_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/board'),
        ),
    ]
