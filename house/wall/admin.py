from django.contrib import admin
from models import *

admin.site.register(Window)
admin.site.register(DoorWay)
admin.site.register(Door)
admin.site.register(Jumper)

class WallMaterialAdminInline(admin.TabularInline): 
    model = WallMaterial
    extra = 1

class WallTypeAdmin(admin.ModelAdmin):
    list_display  = ('name', )
    inlines = (WallMaterialAdminInline, )

class WallWindowAdminInline(admin.TabularInline): 
    model = WallWindow
    extra = 1

class WallDoorAdminInline(admin.TabularInline): 
    model = WallDoor
    extra = 1

class WallDoorWayAdminInline(admin.TabularInline): 
    model = WallDoorWay
    extra = 1

class WallAdmin(admin.ModelAdmin):
    list_display  = ('name', 'type', )
    inlines = (WallWindowAdminInline, WallDoorAdminInline, WallDoorWayAdminInline, )


admin.site.register(WallType, WallTypeAdmin)
admin.site.register(Wall, WallAdmin)

#admin.site.register(Window)
#admin.site.register(Window)
#admin.site.register(Window)
#admin.site.register(Window)
#admin.site.register(Window)
