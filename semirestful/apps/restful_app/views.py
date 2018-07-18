from django.shortcuts import render, redirect
from .models import User

def index(request):
    print('index method')
    context = {
        'all_users' : User.objects.all()
    }
    return render(request, 'restful_app/index.html', context)

def new(request):
    print('new method')
    return render(request, 'restful_app/new.html')

def create(request):
    print('create method')
    print (request.POST)
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email']
    )
    return redirect('/')

def show(request, user_id):
    print('show method')
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, 'restful_app/show.html', context)

def destroy(request, user_id):
    print('destroy method')
    print(user_id)
    User.objects.get(id=user_id).delete()
    return redirect('/')

def edit(request, user_id):
    print('edit method')
    print(user_id)
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, 'restful_app/edit.html', context)

def update(request, user_id):
    print('update method')
    print(request.POST)
    user = User.objects.get(id=user_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    print(user.first_name)
    return redirect('/')