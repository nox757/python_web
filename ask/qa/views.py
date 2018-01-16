from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Question, Answer
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import AskForm, AnswerForm, SignupForm, LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.core.urlresolvers import reverse



# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse("OK")

## url /?page=1
@require_GET
def index(request, *args, **kwargs):
    #Query_set of Questions
    list_questions = Question.objects.order_by("-id")

    #start pagination
    try:
        limit = int(request.GET.get("limit", 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    paginator = Paginator(list_questions, limit)

    try:
        questions = paginator.page(page)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    
    context = {
        "questions": questions,
        "paginator": paginator,
        "limit": limit,
    }
    return render(request, "index.html", context)

@require_GET
def popular(request, *args, **kwargs):
        #Query_set of Questions
    list_questions = Question.objects.order_by("-rating")

    #start pagination
    try:
        limit = int(request.GET.get("limit", 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404
    paginator = Paginator(list_questions, limit)

    try:
        questions = paginator.page(page)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    
    context = {
        "questions": questions,
        "paginator": paginator,
        "limit": limit,
    }
    return render(request, "index.html", context)

#url /question/id/
def question(request, id, ):
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            _ = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(data={ 'question': question.id })
    context = {
        "question": question,
        "form": form,
    }
    return render(request, "question.html", context)


#url /ask/
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    context = {
        'form': form,
    }
    return render(request, 'ask.html', context)


def signup(request):
    if request.method == "POST":
        
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)

            return HttpResponseRedirect(reverse("index"))
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)

def login1(request):
    if request.method == "POST":
        print("us_",request.POST["username"])
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            print(reverse("index"))
            return HttpResponseRedirect(reverse("index"))
    else:
        form = LoginForm()
    
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)




