# Generated by Django 4.1.1 on 2022-10-02 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrontText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('caption', models.CharField(max_length=200)),
                ('btn_text', models.CharField(max_length=20)),
                ('is_event', models.BooleanField(default=False)),
                ('is_activated', models.BooleanField(default=False)),
            ],
        ),
    ]