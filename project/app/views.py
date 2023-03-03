from django.shortcuts import render,redirect
from .models import Adil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import Updateform
from django.contrib import messages

# Create your views here.

def loginUser(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            messages.error(request, 'wrong validation!')
            return redirect('login')
    return render(request, 'app/signin.html')

# def logoutUser(request):
#     logout(request)
#     return redirect('login')

def logoutUser(request):
    logout(request)
    return redirect('login')

def createe(request):
    user = request.user
    # if user.is_superuser:
    adil = Adil.objects.all()
    # else:
    #     adil = Adil.objects.filter(user=user)
    user = request.user
    if request.POST:
       first =  request.POST.get('first')
       last = request.POST.get('last')
       adil.create(user=user, name=first,father=last)
       return redirect('list')


    context = {
        'adil':adil
    }
    return render(request,'app/main.html',context)


def delete(request):
    if request.POST:
        pk = request.POST.get('pk')
        user = Adil.objects.get(id=pk)
        user.delete()
        return redirect('list')


def update(request,pk):
    user = Adil.objects.get(id=pk)
    form= Updateform(instance=user)
    if request.POST:
        form = Updateform(request.POST,instance=user)
        form.save()
        return redirect('list')

    context={
        'form':form
    }

    return render(request,'app/update.html',context)


# def register(request):
#     if request.user.is_authenticated:
#         return redirect('list')
#     if request.POST:
#         username = request.POST.get('username')
#         password1 = request.POST.get('password')
#         password2 = request.POST.get('password2')

        
#         ins =  User.objects.filter(username=username).exists()
#         if ins == True:
#             messages.error(request, 'username already taken')
#             return redirect('register')
            

#         if password1 == password2:
#             user = User.objects.create_user(username=username, password=password1)
#             if user is not None:
#                 user.save()
#                 login(request, user)
#                 return redirect('list')
#         else:
#             messages.error(request, 'Passwords does not match!')
#             return redirect('register')


#     return render(request, 'app/register.html')













def register(request):

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('pasword')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username):
            messages.error(request,'User name is Alredy taken')



        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            if user is not None:
                user.save()

        else:
            messages.error(request,'password dosent match')  
            return redirect('register')  



    return render(request,'app/register.html')

















