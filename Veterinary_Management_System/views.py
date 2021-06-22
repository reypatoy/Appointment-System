from django.contrib import auth
from pathlib import Path

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    # error_message = None
    # form = AuthenticationForm

    return render(request, "auth/login.html", {})