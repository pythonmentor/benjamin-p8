from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from products.models import Favorite
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/login/')
def profile(request):
    return render(request, 'users/profile.html')

def create_account(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/users/profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/create_account.html', {'form': form})

@login_required(login_url='/users/login/')
def favorites_user(request):
    user = request.user
    product_favorite = Favorite.objects.filter(user=user)
    products = [ favorite.id_result for favorite in product_favorite ]

    return render(request, 'users/favorites.html', {'products': products})
