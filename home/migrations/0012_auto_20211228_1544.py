# Generated by Django 3.2.8 on 2021-12-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human_Rights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Peace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Political_participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Carrier',
            new_name='Environment',
        ),
    ]