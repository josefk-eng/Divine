# Generated by Django 4.1.1 on 2022-10-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adwmi', '0009_alter_sermon_placeholder_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_headline', models.BooleanField(default=False)),
                ('headline', models.CharField(max_length=200)),
                ('sub_headline', models.CharField(max_length=200)),
                ('display_image', models.ImageField(blank=True, upload_to='img/news')),
                ('youtube_url', models.CharField(blank=True, max_length=200)),
                ('details', models.CharField(max_length=1000)),
                ('valid_until', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='sermon',
            name='facebook_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='instagram_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='twitter_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='youtube_url',
            field=models.URLField(blank=True),
        ),
    ]