
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import news_post,events,about,administration,gallery
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    indexid = news_post.objects.all()

    length = len(news_post.objects.all())
    return render(request, 'sfuanime/index.html',{"indexid":indexid})
#...
def news(request):

    posts = news_post.objects.all()
    print("news")

    user_list = User.objects.all()
    page = request.GET.get('page', 5)

    paginator = Paginator(posts, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)



    return render(request, 'sfuanime/news.html', {"posts":posts,"users":users})

def event(request):
    eventpost = events.objects.all()

    print("event")
    return render(request, 'sfuanime/event.html',{"eventpost":eventpost})

def membership(request):
    mempost = administration.objects.all()

    print("memebership")
    return render(request, 'sfuanime/membership.html',{"mempost":mempost})


def galleria(request):


    gall = gallery.objects.all()
    return render(request, 'sfuanime/gallery.html', {"gall":gall})

def abouts(request):
    aboutpost = about.objects.all()
    print("about")
    return render(request, 'sfuanime/about.html',{"aboutpost":aboutpost})


def news_index(request, news_id):
    postid = news_post.objects.filter(id = news_id)

    length = len(news_post.objects.all())
    print("postid")
    return render(request, 'sfuanime/news_detail.html',{"postid":postid})
