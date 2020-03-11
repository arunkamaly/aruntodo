from django.contrib import admin

from .models import  *

class TodoeAdmin(admin.ModelAdmin):
	pass

admin.site.register(Todo, TodoeAdmin)

