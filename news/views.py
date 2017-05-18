# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import DetailView
from .models import Article

class NewsView(DetailView):
	model = Article
	template_name = 'article.html'	

def show_news(request, news_id=0, cat_id=0):
	
	return render(request, 'blabla.html', {"news_id": news_id})