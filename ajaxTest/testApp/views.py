from django.shortcuts import render
from django.http import HttpResponse

from requests_oauthlib import OAuth1
import requests
import json

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def return_tweets(request):
    APIKey = ''
    APISecret = ''
    AccessToken = ''
    AccessTokenSecret = ''

    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

    auth = OAuth1(APIKey, APISecret, AccessToken, AccessTokenSecret)
    username = request.GET.get('handle_data')
    verificationUrl = ' https://api.twitter.com/1.1/users/show.json?screen_name=%s' %username
    response = requests.get(verificationUrl, auth=auth)
    tweets = []

    if response.status_code == 200:
        requestUrl = ' https://api.twitter.com/1.1/statuses/user_timeline.json?tweet_mode=extended&screen_name=%s&count=10' %username
        r = requests.get(requestUrl, auth=auth,)
        for tweet in r.json():
            tweets.append(tweet['full_text'])
    else:
        tweets.append("Invalid Handle")

    response_data = {'tweet_data' : tweets}
    return HttpResponse(json.dumps(response_data))
