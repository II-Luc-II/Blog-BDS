from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms.CustomUserLoginForm import CustomUserLoginForm
from account.forms.CustomUserRegisterForm import CustomUserRegisterForm
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vous êtes bien enregistré')
            return redirect('login')
    else:
        form = CustomUserRegisterForm()

    return render(request, 'registration/register.html', {"form": form})


def login_user(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Vous êtes bien connecté.')
                return redirect('home')
            else:
                messages.error(request, 'Les identifiants sont incorrects.')
        else:
            messages.error(request, 'Merci de corriger les erreurs dans le formulaire.')
    else:
        form = CustomUserLoginForm()

    return render(request, 'registration/login.html', {"form": form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Vous êtes bien déconnecté.')
    return redirect('home')


def password_reset_user(request):
    if request.method == 'POST':
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Merci de saisir votre adresse mail.')
            return redirect('password_reset_done')
        else:
            messages.error(request, "Merci de saisir une adresse mail valide")
    form = PasswordResetForm()

    return render(request, 'registration/templates/password_reset.html', {"form": form})


def password_reset_user_done(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Merci de saisir votre adresse mail.')
            return redirect('password_reset_done')
        else:
            messages.error(request, "Merci de saisir une adresse mail valide")
    form = PasswordResetForm()

    return render(request, 'registration/templates/password_reset.html', {"form": form})

