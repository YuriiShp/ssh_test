from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Album)
admin.site.register(PlayList)
admin.site.register(Song)
admin.site.register(Genre)
