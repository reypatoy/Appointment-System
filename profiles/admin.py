from django.contrib import admin
from .models import User, Admin, staff, customer


# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(staff)
admin.site.register(customer)
