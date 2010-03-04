from django.contrib import admin
from models import *

class WallingMaterialTypeAdmin(admin.ModelAdmin):
    list_display  = ('name',  )

admin.site.register(WallingMaterialType, WallingMaterialTypeAdmin)
admin.site.register(WallingMaterial)
admin.site.register(SlurryMaterialType)
admin.site.register(SlurryMaterial)
admin.site.register(Armature)
