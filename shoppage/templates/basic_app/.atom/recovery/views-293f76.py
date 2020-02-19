from django.shortcuts import render
import json
# Create your views here.
import urllib.request
from city_list_json.city.list.json import *

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
        )
