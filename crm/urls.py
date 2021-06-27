from django.conf import settings
from django.urls import path
from django.urls import path
from django.contrib.auth import views

from .views import admin_dashboard_view


app_name = 'crm'

urlpatterns = [
    path('dashboard/', admin_dashboard_view, name='admin_dashboard_view'),
    # logout
    # path('logout/', logout, name='logout')

]
