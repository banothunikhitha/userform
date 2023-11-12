# userform/views.py
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_data')
    else:
        form = UserForm()
    return render(request, 'userform/user_form.html', {'form': form})

def user_data(request):
    data = User.objects.all()
    return render(request, 'userform/user_data.html', {'user_list': data})
