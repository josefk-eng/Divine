from django.shortcuts import render

from .models import FrontText, \
    BackgroundVideo, \
    Ministry, \
    Sermon, \
    News, \
    Person, \
    WSchedule, \
    WelcomeNote, \
    Project, About, Teams

# Create your views here.
def index(request):
    slides = FrontText.objects.all()
    background_video =   BackgroundVideo.objects.all().first()
    ministries = Ministry.objects.all()
    sermons = Sermon.objects.all()
    news = News.objects.all()
    headline = news.filter(isheadline = True).first
    people = Person.objects.all()
    pastors = people.filter(title = "pastor")
    events = WSchedule.objects.all()
    notes = WelcomeNote.objects.all()
    projects = Project.objects.all()
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    params = {
        'slides':slides, 
        'bg_vid':background_video, 
        'ministries':ministries, 
        'sermon':sermons, 
        'news':news, 
        'headline':headline,
        'nbar': 'home',
        'pastors':pastors,
        'events':events,
        'days':days,
        'notes':notes,
        'projects':projects
        }
    return render(request, 'index.html',params)

def about(request):
    aboutt = About.objects.first()
    teams = Teams.objects.all()
    params = {
        'nbar':'about',
        'about':aboutt,
        'teams':teams
    }
    return render(request, 'about.html',params)

def contact(request):
    params = {
        'nbar':'contact'
    }
    return render(request, 'contact.html',params)
