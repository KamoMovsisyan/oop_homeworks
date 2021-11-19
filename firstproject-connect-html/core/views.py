from django.shortcuts import HttpResponse, render
from datetime import datetime
from core.models import Task


def hello(request):
    return HttpResponse('<h1>Hello Django World!</h1>')


def intro(request):
    return HttpResponse('<center><h1>Name : Kamo<br/>Surname : Movsisyan<br/>School : PhysMath</h1></center>')


def time_(request):
    time_now = datetime.now()
    return HttpResponse(f'<center><h1>{time_now}</h1></center>')


def solution(request):
    my_dict = {i: i*i for i in range(1, 16)}
    return HttpResponse(f'<h1>{my_dict}</h1>')


def list_task(request):
    tasks = Task.objects.all()
    html = f'''
    <h2>tasks</h2>
    <h3>task_1: {tasks[0]} </h2>
    <h3>task_2: {tasks[1]}</h2>
    '''

    return HttpResponse(html)


def home(request):
    # show = Task.objects.all()

    # return HttpResponse(show)

    return render(request, "core/home.html")


def create_task(request):
    pass


def homework(request):

    return render(request, "core/index_homework.html")
