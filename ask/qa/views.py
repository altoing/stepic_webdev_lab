from django.shortcuts import render
from django.views.generic import DetailView
from django.http import Http404
# Create your views here.

from django.http import HttpResponse
from .models import Users, Question

class NewsView(DetailView):
    model = Users

def test(request, *args, **kwargs):
    return HttpResponse('OK TEST')

def mainpage (request):
    latest_question_list = Question.objects.order_by("-added_at")[:10]
    output = '<br>'.join([q.text for q in latest_question_list])
    return HttpResponse(output)

def popular(request, *args, **kwargs):
    latest_question_list = Question.objects.order_by("rating")[:10]
    output = '<br>'.join([q.text for q in latest_question_list])
    return HttpResponse(output)

def question(request, id=None):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'question.html', {'question': question})