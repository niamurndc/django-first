from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):

  if request.method == 'POST':
    firstName = request.POST['firstname']
    lastName = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password1']
    cpassword = request.POST['password2']

    if password == cpassword:
      if User.objects.filter(username = username).exists():
        messages.info(request, 'Username Taken')
        return redirect('register')
      elif User.objects.filter(email = email).exists():
        messages.info(request, 'Email already used')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstName, last_name=lastName)
        user.save()
        print('user created')
        return redirect('/')
    else:
      messages.info(request, 'Password not match')
    return redirect('register')
  else:
    return render(request, 'register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Invalid Username and Password')
      return redirect('login')
  else:
    return render(request, 'login.html')


def logout(request):
  auth.logout(request)
  return redirect('/')