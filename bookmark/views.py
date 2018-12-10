#from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView  # 추가
#from django.shortcuts import get_object_or_404, render  # 추가
from bookmark.models import Bookmark

# Class Based View 버전
class BookmarkLV(ListView):
    model = Bookmark
  #  bookmark_list = BookmarkLV.as_view()

class BookmarkDV(DetailView):
    model = Bookmark
  #  bookmark_detail = BookmarkDV.as_view()