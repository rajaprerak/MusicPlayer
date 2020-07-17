from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Favourite)
admin.site.register(Recent)