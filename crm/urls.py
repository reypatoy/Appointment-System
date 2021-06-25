from django.urls import path
from django.urls import path

from .views import admin_dashboard_view


app_name = 'crm'

urlpatterns = [
    path('/dashboard', admin_dashboard_view, name='admin_dashboard_view')

]
