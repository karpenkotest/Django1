from django.shortcuts import render
from django.http import HttpResponse
def predictions_view(request):
    return HttpResponse('You will have a great day! Have fun!')
def empty_view(request):
    return HttpResponse('If you want to see your future - add /prediciton or /random to the url')

def random_view(request):
    import random
    random_number = random.randint(0, 5)
    if random_number == 0: return HttpResponse("Stay at home")
    if random_number == 2: return HttpResponse("Go to work")
    if random_number ==3: return HttpResponse("Go to gym")
    if random_number == 4: return  HttpResponse( "Buy a ticket to Ukraine")
    if random_number == 5: return HttpResponse("Buy a ticket to Paris")

def nested_view(request):
    return HttpResponse("Simple test")

def index_view(request):
    return render(request, 'index.html')
def depends_on_number_in_url_view(request,some_number):
    return HttpResponse(f'Number in ulr is {some_number}')
