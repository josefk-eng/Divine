# Generated by Django 4.1.1 on 2022-10-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ministry',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='ministry',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='ministry',
            name='number',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='ministry',
            name='story',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
