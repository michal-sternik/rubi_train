from django.contrib import admin
from .models import CubeType, UserResults
@admin.register(UserResults)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "cubetype","user","time")
admin.site.register(CubeType)