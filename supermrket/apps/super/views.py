from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'Supermarket/login.html')


def reg(request):
    return render(request, 'Supermarket/reg.html')


def cs(request):
    return HttpResponse('ok')
