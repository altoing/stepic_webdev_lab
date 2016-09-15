from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.

from django.http import HttpResponse
from .models import Users

class NewsView(DetailView):
    model = Users

def test(request, *args, **kwargs):
    return HttpResponse('OK')