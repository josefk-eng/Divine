from django.contrib import admin
from .models import FrontText,\
    BackgroundVideo, \
    Ministry, \
    Person, \
    Project, \
    Sermon, \
    WSchedule, \
    WelcomeNote,\
    News, \
    About, Teams

# Register your models here.
admin.site.register(FrontText)
admin.site.register(BackgroundVideo)
admin.site.register(Ministry)
admin.site.register(Sermon)
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(WSchedule)
admin.site.register(WelcomeNote)
admin.site.register(News)
admin.site.register(About)
admin.site.register(Teams)