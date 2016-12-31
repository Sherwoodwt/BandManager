from django.contrib import admin

from .models import Band, Member, Song, Task
# Register your models here.

admin.site.register(Band)
admin.site.register(Member)
admin.site.register(Song)
admin.site.register(Task)
