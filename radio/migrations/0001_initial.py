# Generated by Django 3.2.8 on 2022-01-17 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name_en', models.CharField(max_length=100)),
                ('season_image', models.ImageField(blank=True, null=True, upload_to='static/img/season')),
            ],
        ),
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_name_en', models.CharField(max_length=100)),
                ('episode_image', models.ImageField(blank=True, null=True, upload_to='static/img/episode')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.all_season')),
            ],
        ),
    ]
