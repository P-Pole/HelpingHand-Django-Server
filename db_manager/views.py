from django.shortcuts import get_object_or_404, render, redirect
from django.core.files import File 
from django.core.files.temp import NamedTemporaryFile
from charities.models import Charities, User
from .forms import CharityForm, UserForm
import requests


def charity_list(request, pk=None):
    charities = Charities.objects.all()

    if request.method == 'POST':
        if pk:
            charity = get_object_or_404(Charities, pk=pk)
            form = CharityForm(request.POST, instance=charity)
        else:
            form = CharityForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('charity_list')

    if pk:
        charity = get_object_or_404(Charities, pk=pk)
        form = CharityForm(instance=charity)
    else:
        form = CharityForm()

    return render(request, 'charity_list.html', {'charities': charities, 'form': form})

def charity_delete(request, pk):
    charity = get_object_or_404(Charities, pk=pk)
    charity.delete()
    return redirect('charity_list')



def user_list(request, pk=None):
    users = User.objects.all()

    if request.method == 'POST':
        if pk:
            user = get_object_or_404(User, pk=pk)
            form = UserForm(request.POST, instance=user)
        else:
            form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user_list')

    if pk:
        user = get_object_or_404(User, pk=pk)
        form = UserForm(instance=user)
    else:
        form = UserForm()

    return render(request, 'user_list.html', {'users': users, 'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user_list')

