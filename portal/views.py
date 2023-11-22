from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from administracion.models import Product
from django.contrib.auth.models import Group

def index(request):
    return render(request, './portal/index.html')


def productos(request):
    products = Product.objects.all()
    return render(request, './portal/productos.html', {'productos': products})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Usuario')
            user.groups.add(group)
            return redirect('login')
        errors = form.errors
        form = SignUpForm(request.POST)
        return render(request, './portal/usuarios/signup.html', {'form': form, 'errors': errors})
    else:
        form = SignUpForm()
        return render(request, './portal/usuarios/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            errors = "Credenciales incorrectas."
            return render(request, './portal/usuarios/login.html', {'errors': errors})
    return render(request, './portal/usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def profile_view(request):
    pass

def update_profile_view(request):
    pass