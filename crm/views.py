from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.


def admin_dashboard_view(request):
    return render(request, 'crm/admin_dashboard.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/')
