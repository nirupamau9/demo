from django.contrib import admin
from .models import District, Branch

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'wikipedia_link')

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'name': ('name',)}

admin.site.register(District, DistrictAdmin)
admin.site.register(Branch, BranchAdmin)
