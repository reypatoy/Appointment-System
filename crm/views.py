from django.shortcuts import render

# Create your views here.


def admin_dashboard_view(request):
    return render(request, 'crm/admin_dashboard.html')
