from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Assignment, User

class AssignmentAdmin(admin.ModelAdmin):
    #fields = ('title', 'created_date', 'expire_date', 'earning', 'creator')
    list_display = ('title', 'expire_date', 'earning', 'creator')
    list_filter = ('creator',)

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(User, UserAdmin)

admin.site.site_header = _('DataX Administration')
admin.site.site_title = _('DataX Site Administration')