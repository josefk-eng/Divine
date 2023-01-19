from django.db import models
from django.utils import timezone
from .formatChecker import ContentTypeRestrictedFileField


# Create your models here.
class FrontText(models.Model):
    header = models.CharField(max_length=1000)
    caption = models.CharField(max_length=1000)
    big_caption = models.CharField(max_length=1000, default="")
    btn_text = models.CharField(max_length=20)
    is_event = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=False)
    back_image = ContentTypeRestrictedFileField(upload_to='videos/carousel', content_types=['png','jpeg','jpg'],max_upload_size=1000000)


class BackgroundVideo(models.Model):
    caption = models.CharField(max_length=100)
    video = ContentTypeRestrictedFileField(upload_to='videos/carousel', content_types=['mp4','mov'],max_upload_size=3000000,blank=True, null=True)

    def __str__(self):
        return self.caption


class Ministry(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    story = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=200, blank=True)
    number = models.CharField(max_length=200, blank=True)
    ministry_image = ContentTypeRestrictedFileField(upload_to='img/ministries', content_types=['png','jpeg','jpg'],max_upload_size=1000000)

    def __str__(self):
        return self.name


class Sermon(models.Model):
    name = models.CharField(max_length=200)
    preacher = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    placeholder_image = ContentTypeRestrictedFileField(upload_to='img/sermons', content_types=['png','jpeg','jpg'],max_upload_size=1000000)
    youtube_url = models.URLField(max_length=200, blank=True)
    facebook_url = models.URLField(max_length=200, blank=True)
    twitter_url = models.URLField(max_length=200, blank=True)
    instagram_url = models.URLField(max_length=200, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class News(models.Model):
    isheadline = models.BooleanField(default=False)
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200)
    display_image = ContentTypeRestrictedFileField(upload_to='img/news', content_types=['png','jpeg','jpg'],max_upload_size=1000000)
    youtube_url = models.CharField(max_length=200, blank=True)
    details = models.CharField(max_length=1000)
    valid_until = models.DateField()

    def __str__(self):
        return self.headline


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    display_image = ContentTypeRestrictedFileField(upload_to='img/projects', content_types=['png','jpeg','jpg'],max_upload_size=1000000)


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    is_drop = models.BooleanField(default=False)
    drop_list = models.CharField(max_length=100)


class About(models.Model):
    big_header = models.CharField(max_length=100, default="Annointed Divine Word Ministries International")
    sub_header = models.CharField(max_length=100, default="A Place Where Ministers Are Made")
    text_before_bullets = models.CharField(max_length=500)
    text_bullets = models.CharField(max_length=1000, blank=True, null=True)
    text_after_bullets = models.CharField(max_length=500, blank=True, null=True)
    vision = models.CharField(max_length=300, default="Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi")
    mission = models.CharField(max_length=300, default="Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi")
    core_values = models.CharField(max_length=300, default="Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi")


class WSchedule(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    event_image = ContentTypeRestrictedFileField(upload_to='img/events', content_types=['png','jpeg','jpg'],max_upload_size=500000)
    event_video = models.URLField(max_length=200, blank=True)
    contact_person = models.CharField(max_length=100)


class Teams(models.Model):
    team_image = ContentTypeRestrictedFileField(upload_to='img/teams', content_types=['png','jpeg','jpg'],max_upload_size=1000000, blank=True)
    team_name = models.CharField(max_length=100)
    team_slogan = models.CharField(max_length=100)


class Person(models.Model):
    names = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    story = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=200, blank=True)
    number = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField(blank=True)
    role = models.CharField(max_length=200, default='member')
    title = models.CharField(max_length=200, default='Brethren')
    profile_image = models.ImageField(upload_to="img/persons")
    full_image = ContentTypeRestrictedFileField(upload_to='img/full/persons', content_types=['png','jpeg','jpg'],max_upload_size=1000000)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.names


class WelcomeNote(models.Model):
    full_image = ContentTypeRestrictedFileField(upload_to='img/welcome', content_types=['png','jpeg','jpg'],max_upload_size=1000000)
    header = models.CharField(max_length=200)
    note = models.CharField(max_length=500)

    def __str__(self):
        return self.header

