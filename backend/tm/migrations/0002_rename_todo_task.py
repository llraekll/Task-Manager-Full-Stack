# Generated by Django 4.1.2 on 2022-10-11 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tm', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Task',
        ),
    ]
