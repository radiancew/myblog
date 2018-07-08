from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def index_view(request):
    return render(request, 'base.html')
