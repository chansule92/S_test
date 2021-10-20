from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user_list, result
from django.db.models import Q


def home(request):
    list=None
    query=None
    if 'word' in request.GET:
        query=request.GET.get('word')
        list=user_list.objects.values().filter(Q(id__icontains=query)|Q(user__icontains=query))

    if request.method == 'POST':
        post=user_list()
        post.user=request.POST.get('user')
        post.save()

        return redirect(start)
    else:
        post=user_list.objects.values_list()

    a = len(result.objects.filter(answer = 'f').values_list('user_id'))
    complete_user=[]
    for i in range(0,a):
        complete_user.append(result.objects.filter(answer = 'f').values_list('user_id')[i][0])

    b = len(user_list.objects.values_list())
    all_user = []
    for i in range(0,b):
        all_user.append(user_list.objects.values_list('id')[i][0])

    fail_user= set(all_user) - set(complete_user)
    for i in fail_user:
        user_list.objects.filter(id = i).delete()
        result.objects.filter(user_id = i).delete()

    return render(request, 'science/home.html', {'post':post, 'list':list })

def start(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='start'
        post.answer=request.POST.get('answer')
        post.save()
        if request.POST.get('answer')=='y':
            return redirect(question0)
        elif request.POST.get('answer')=='n':
            return redirect(question1)
    content={'user':user}
    return render(request, 'science/start.html',content)

def question0(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='0'
        post.answer=request.POST.get('answer')
        post.save()
        if request.POST.get('answer')=='y':
            return redirect(final0)
        elif request.POST.get('answer')=='n':
            return redirect(question1_1)

    return render(request, 'science/question0.html')

def question1(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='1'
        post.answer=request.POST.get('answer')
        post.save()
        if request.POST.get('answer')=='y':
            return redirect(question1_1)
        elif request.POST.get('answer')=='n':
            return redirect(question2)
    return render(request, 'science/question1.html')

def question1_1(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='1_1'
        post.answer=request.POST.get('answer')
        post.save()
        if request.POST.get('answer')=='y':
            return redirect(final1)
        elif request.POST.get('answer')=='n':
            return redirect(question2_1)
    return render(request, 'science/question1_1.html')


def question2(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='2'
        post.answer=request.POST.get('answer')
        post.save()
        if request.POST.get('answer')=='y':
            return redirect(question2_1)
        elif request.POST.get('answer')=='n':
            return redirect(final4)
    return render(request, 'science/question2.html')

def question2_1(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='2_1'
        post.answer=request.POST.get('answer')
        post.save()
        if request.POST.get('answer')=='y':
            return redirect(final2)
        elif request.POST.get('answer')=='n':
            return redirect(final3)
    return render(request, 'science/question2_1.html')

def final0(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='f0'
        post.answer=request.POST.get('answer')
        post.save()
        return redirect(home)

    return render(request, 'science/final0.html')

def final1(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='f1'
        post.answer=request.POST.get('answer')
        post.save()
        return redirect(home)

    return render(request, 'science/final1.html')


def final2(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='f2'
        post.answer=request.POST.get('answer')
        post.save()
        return redirect(home)

    return render(request, 'science/final2.html')

def final3(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='f3'
        post.answer=request.POST.get('answer')
        post.save()
        return redirect(home)

    return render(request, 'science/final3.html')

def final4(request):
    user=user_list.objects.values().last()
    if request.method == 'POST':
        post = result()
        post.user_id=user['id']
        post.user=user['user']
        post.question='f4'
        post.answer=request.POST.get('answer')
        post.save()
        return redirect(home)

    return render(request, 'science/final4.html')

def outcome(request,id):
    list=None
    query=None
    if 'word' in request.GET:
        query=request.GET.get('word')
        list=user_list.objects.values().filter(Q(id__icontains=query)|Q(user__icontains=query))

    content = result.objects.filter(user_id = id).values()
    return render(request, 'science/outcome.html',{'content':content, 'list':list})
