from django.contrib import admin
from .models import *


class Armed_universityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'full_info', 'main_img', 'location', 'is_published', 'time_create', 'time_update', 'contacts', 'website')
    readonly_fields = ('time_create', 'time_update')
    save_on_top = True


admin.site.register(Armed_university, Armed_universityAdmin)
