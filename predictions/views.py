from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from random import randint


def depends_on_number_in_url_view(request,some_number, slug_text=None):
    result=""
    if (some_number%2)==0:
        result="Even"
    else:
        result="Odd"

    context={'result':result,
             'text':slug_text,
             'number':randint(0,100)
    }
    return render(request,'depends_on_number.html', context)


def predictions_view(request):
    return HttpResponse('You will have a great day! Have fun!')
def empty_view(request):
    return HttpResponse('If you want to see your future - add /prediciton or /random to the url')

def random_view(request):
    random_number = randint(0, 6)
    response = 'Learn Python'
    response_dict={
        0:"Stay at home",
        1:"Go to work",
        2:"Go to gym",
        3: "Buy a ticket to Ukraine",
        4: "Buy a ticket to Paris",
        5: "Drink a coffe",
        6: "Watch a favorite film"
    }
    response=response_dict.get(random_number)
    return HttpResponse(response)
def nested_view(request):
    return HttpResponse("Simple test")

def index_view1(request):
    context = {"time": datetime.now()}
    return render(request, 'index.html', context)

def dashboard_view(request):
    return render(request, 'dashboard.html')

def writers_view(request):
    return render(request, 'writers.html')

def article_view(request):
    return render(request, 'Article.html')


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s

def index_view(request):
    my_num = 33
    my_str = 'Yuliia'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    data = {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
    }
    return render(
        request,
        'index.html',
        data
    )