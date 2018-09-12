from django.contrib import admin
from .models import User, Dishe, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Dishe)
admin.site.register(Order)