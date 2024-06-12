from django.contrib import admin
from hackathonprat.models import MiUser

class MiUserAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(MiUser,MiUserAdmin)