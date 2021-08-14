from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from products.models import Customer
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            name = form.cleaned_data.get('first_name')
            Customer.objects.get_or_create(user=user,email=email,name=name)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
