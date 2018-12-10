"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite2.views import HomeView
#from django.views.generic import ListView, DetailView
#from bookmark.models import Bookmark


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^$', HomeView.as_view(), name = 'home') #추가

    #url(r'^bookmarks/$', ListView.as_view(model=Bookmark), name='index'),
    #url(r'^bookmarks/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name='detail'),
]

