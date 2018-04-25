from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    url(r'^ajax/returntweets/$', views.return_tweets, name = 'returnTweets'),
]
