# Generated by Django 3.2.8 on 2021-11-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_news_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/home')),
            ],
        ),
    ]