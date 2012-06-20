from django.contrib import admin
from photos.models import Gallery
from photos.models import Photo
 
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
 
admin.site.register(Gallery, GalleryAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'filename', 'created')

admin.site.register(Photo, PhotoAdmin)


