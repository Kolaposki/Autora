from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def logout_user(request):
    print("logging out ", request.user)
    logout(request)
    return redirect(reverse('home'))
