# Generated by Django 3.2.8 on 2021-12-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211110_1423'),
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
            name='Carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Partnerships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('bio_en', models.TextField()),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_name_en', models.CharField(max_length=200)),
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
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WelcomeScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/welcome')),
            ],
        ),
    ]
