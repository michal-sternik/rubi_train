from django.contrib import admin
from .models import CubeType, UserResults
# Register your models here.
@admin.register(UserResults)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "cubetype","user","time")
# admin.site.register(CubeType)
admin.site.register(CubeType)