from django.shortcuts import render
from django.http import HttpResponse
from .models import result

def home(request):
    if request.method == 'POST':
        result=result()
        result.text=request.POST['text']
        result.save()
        return redirect('result')
    else:
        result=result.objects.all()
        return render(request, 'science/start.html',{'result':result})
