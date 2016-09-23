from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Users, Question, Answer
from .forms import AskForm, AnswerForm, LoginForm

class NewsView(DetailView):
    model = Users

def test(request, *args, **kwargs):
    return HttpResponse('OK TEST')

def mainpage2 (request):
    question_list = Question.objects.new()
    links_list = []
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(question_list, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    posts = page.object_list

    for q in posts:
        links_list.append("/question/{}/".format(q.pk))
    ziplist = zip(posts, links_list)

    return render(request, 'mainpage2.html', {
        "posts": page.object_list,
        "paginator": paginator,
        "page": page,
        "ziplist": ziplist,
        }, content_type="text/html")

def popular(request, *args, **kwargs):
    question_list = Question.objects.popular()
    links_list = []
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(question_list, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    posts = page.object_list

    for q in posts:
        links_list.append("/question/{}/".format(q.pk))
    ziplist = zip(posts, links_list)

    return render(request, 'popular.html', {
        "posts": page.object_list,
        "paginator": paginator,
        "page": page,
        "ziplist": ziplist,
        }, content_type="text/html")

def question(request, id=None):
    if request.method =='POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            newanswer = Answer(text=text, question_id=id, author=User.objects.get(username=request.user.username))
            newanswer.save()
            return HttpResponseRedirect('/question/{}'.format(id))
    else:
        form = AnswerForm()
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    answer_list  = Answer.objects.filter(question_id=id)

    return render(request, 'question.html', {'question': question, 'answer_list': answer_list, 'form': form})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            newquestion = Question(title=title, text=text, author=User.objects.get(username=request.user.username))
            newquestion.save()
            pk = newquestion.pk
            return HttpResponseRedirect('/question/{}'.format(pk))
    else:
        form = AskForm()

    return render(request, 'ask.html', {'form': form})

def auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponse('DEBUG')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/')