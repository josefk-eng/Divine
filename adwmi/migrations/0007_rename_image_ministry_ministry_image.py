# Generated by Django 4.1.1 on 2022-10-04 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adwmi', '0006_ministry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ministry',
            old_name='image',
            new_name='ministry_image',
        ),
    ]
