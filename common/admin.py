from django.contrib import admin
from .models import State, City, Area
# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_del', 'created_at', 'updated_at')
    list_filter = ('is_del',)
    search_fields = ('name','id')
    ordering = ('id',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_del',  'state','created_at', 'updated_at')
    list_filter = ('is_del',)
    search_fields = ('name','id')
    ordering = ('id',)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_del', 'category', 'city', 'created_at', 'updated_at')
    list_filter = ('is_del',)
    search_fields = ('name','id')
    ordering = ('id',)