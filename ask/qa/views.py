from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Question, Answer
from django.http import Http404
from django.core.paginator import Paginator




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
def question(request, id):
     try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    
    context = {
        "question": question,
    }
     return render(request, "question.html", context)


