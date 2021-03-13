from django.contrib import admin
from .models import photo
# Register your models here.
@admin.register(photo)
class photoadmin(admin.ModelAdmin):
    list_display = ['id','photo','name','date']