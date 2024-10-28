from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.shortcuts import render, HttpResponse


@csrf_exempt
def login(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        print(username, password)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})




def show(request):
    return HttpResponse('Hello, world. You\'re at the polls view.')
