# djapps.main.admin
from django.contrib import admin
from .models import AboutMe

admin.ModelAdmin.save_on_top = True


class AboutMeAdmin(admin.ModelAdmin):
    pass


admin.site.register(AboutMe, AboutMeAdmin)