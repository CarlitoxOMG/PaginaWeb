from django.contrib import admin
from .models import Mascota, Dueño

# Register your models here.
admin.site.register(Dueño)
admin.site.register(Mascota)
