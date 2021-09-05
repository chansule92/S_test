from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user_list

def home(request):
    if request.method == 'POST':
        post=user_list()
        post.user=request.POST.get('user')
        post.save()
        return redirect(start)
    else:
        post=user_list.objects.all()
        return render(request, 'science/home.html',{'post':post})

def start(request,id):

        return render(request, 'science/start.html')
