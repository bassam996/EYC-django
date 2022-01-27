# Generated by Django 3.2.8 on 2022-01-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/cadres')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('job_en', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('university_en', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('bio_en', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/radio')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/tech')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
    ]
