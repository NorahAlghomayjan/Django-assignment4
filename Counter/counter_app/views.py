from ast import excepthandler
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if ('actual_count' in request.session):
        request.session['actual_count'] += 1
    else:
        request.session['actual_count'] = 0

    if ('counter' in request.session):
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0

    context = {
        'counter': request.session['counter'],
        'actual_count':request.session['actual_count']
    }
    return render(request, 'index.html', context)


def destroy_session(request):
    if 'counter' in request.session:
        del request.session['counter']

    return redirect('/')


def increment2(request):
    request.session['counter'] += 2
    context = {
        'counter': request.session['counter'],
        'actual_count':request.session['actual_count']
    }

    return render(request,'index.html',context)


def userCount(request):
    request.session['counter']= int(request.POST.get('userCount'))
    context = {
        'counter': request.session['counter'],
        'actual_count':request.session['actual_count']
    }
    return render(request,'index.html',context)