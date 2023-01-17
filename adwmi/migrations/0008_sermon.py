# Generated by Django 4.1.1 on 2022-10-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adwmi', '0007_rename_image_ministry_ministry_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('preacher', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('placeholder_image', models.CharField(max_length=200)),
                ('youtube_url', models.URLField()),
                ('facebook_url', models.URLField()),
                ('twitter_url', models.URLField()),
                ('instagram_url', models.URLField()),
            ],
        ),
    ]
