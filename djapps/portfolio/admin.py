# djapps.portfolio.admin
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Skill, Work

admin.ModelAdmin.save_on_top = True


class SkillAdmin(SortableAdminMixin, AdminImageMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = (
        'name',
        'group',
    )
    list_filter = ('group',)
    

class WorkAdmin(SortableAdminMixin, AdminImageMixin, admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('name',)


admin.site.register(Skill, SkillAdmin)
admin.site.register(Work, WorkAdmin)