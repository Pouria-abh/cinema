from django.contrib import admin
from .models import Movie , Gener , CinemaHall ,ShowTimes

# Register your models here.

@admin.register(Movie)
class MovieAdminModel(admin.ModelAdmin):
    list_display=['title','is_active','expire_at']
    list_editable=['is_active']

admin.site.register(Gener)   
    
@admin.register(CinemaHall)
class CinemaHallAdminModel(admin.ModelAdmin):
    list_display=['name','capacity']
    list_editable=['capacity']

@admin.register(ShowTimes)
class CinemaHallAdminModel(admin.ModelAdmin):
    list_display=['movie','hall','time']
    list_editable=['time','hall']  
 
