from django.contrib import admin
from models import *

class FloorWallInline(admin.TabularInline): 
    model = FloorWall
    extra = 1

class FloorAdmin(admin.ModelAdmin):
    list_display  = ('type', 'height', )
    inlines = (FloorWallInline, )

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ['name'], }

admin.site.register(Floor, FloorAdmin)
admin.site.register(Building, BuildingAdmin)
