from Veterinary_Management_System.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import login_view, home_view, appointment_view, signup_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # login
    path('login/', login_view, name='login_view'),
    # home
    path('home/', home_view, name='home_view'),
    # appointment
    path('appointments/', appointment_view, name='appointment_view'),
    # crm
    path('crm/', include('crm.urls', namespace='crm')),
    # signup
    path('signup/', signup_view, name='signup_view')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
