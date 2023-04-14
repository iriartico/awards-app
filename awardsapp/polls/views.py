from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    return HttpResponse(f"You are looking at question number {question_id}")


def results(request, question_id):
    return HttpResponse(f"You are looking the result of the question number {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting for question number {question_id}")