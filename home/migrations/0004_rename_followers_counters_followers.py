# Generated by Django 3.2.8 on 2021-11-08 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_counters_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counters',
            old_name='Followers',
            new_name='followers',
        ),
    ]
