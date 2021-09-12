from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user_list, result

def home(request):
    if request.method == 'POST':
        post=user_list()
        post.user=request.POST.get('user')
        post.save()

        return redirect(start)
    else:
        post=user_list.objects.values_list()
    return render(request, 'science/home.html',{'post':post})

def start(request):
        user=user_list.objects.values().last()
        if request.method == 'POST':
            result = result()
            result.user_id=user[0]
            result.user=user[1]
            result.question=1
            result.answer=request.POST.get('answer')
            result.save()
            if request.POST.get('answer')=='y':
                redirect(second1)
            elif request.POST.get('answer')=='n':
                redirect(second2)

        content={'user':user}
        return render(request, 'science/start.html',content)

def second1(request):

    return render(request, 'science/1-2.html')

def second2(request):

    return render(request, 'science/2-1.html')
