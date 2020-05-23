
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import news_post,events,about,administration

def index(request):

    indexid = news_post.objects.all()

    length = len(news_post.objects.all())
    return render(request, 'sfuanime/index.html',{"indexid":indexid})
#...
def news(request):

    posts = news_post.objects.all()
    print("news")
    return render(request, 'sfuanime/news.html', {"posts":posts})

def event(request):
    eventpost = events.objects.all()

    print("event")
    return render(request, 'sfuanime/event.html',{"eventpost":eventpost})

def membership(request):
    mempost = administration.objects.all()

    print("memebership")
    return render(request, 'sfuanime/membership.html',{"mempost":mempost})


def gallery(request):

    return render(request, 'sfuanime/gallery.html')

def abouts(request):
    aboutpost = about.objects.all()
    print("about")
    return render(request, 'sfuanime/about.html',{"aboutpost":aboutpost})


def news_index(request, news_id):
    postid = news_post.objects.filter(id = news_id)

    length = len(news_post.objects.all())
    print("postid")
    return render(request, 'sfuanime/news_detail.html',{"postid":postid})
