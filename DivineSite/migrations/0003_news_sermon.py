# Generated by Django 4.1.1 on 2022-10-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DivineSite', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('expiry_date', models.DateField(max_length=200)),
                ('image_url', models.URLField()),
                ('youtube_url', models.URLField()),
                ('facebook_url', models.URLField()),
                ('twitter_url', models.URLField()),
                ('instagram_url', models.URLField()),
            ],
        ),
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
