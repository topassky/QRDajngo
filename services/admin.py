from django.contrib import admin
from .models import Service

# Register your models here.
#class CategoryAdmin(admin.ModelAdmin):
 #   readonly_fields = ('created', 'updated')


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
#admin.site.register(Category, CategoryAdmin)