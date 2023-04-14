from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home Page of Awards App")


def detail(request, question_id):
    return HttpResponse(f"You are looking at question number {question_id}")


def results(request, question_id):
    return HttpResponse(f"You are looking the result of the question number {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting for question number {question_id}")