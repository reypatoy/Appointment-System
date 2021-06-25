from django.contrib import auth
from pathlib import Path

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    error_message = None
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            if request.GET.get('next'):
                return redirect(request.GET.get('next'))

            else:
                if user.user_type == 1:
                    return redirect('crm:admin_dashboard.html')

    return render(request, "auth/login.html", {})


def home_view(request):
    return render(request, "pages/home.html")


def appointment_view(request):
    return render(request, 'pages/appointment.html')
