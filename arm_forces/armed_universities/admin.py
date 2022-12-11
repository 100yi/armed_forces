from django.contrib import admin
from .models import *


class Armed_universityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'country')


admin.site.register(Armed_university, Armed_universityAdmin)
