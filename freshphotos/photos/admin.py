from django.contrib import admin
from photos.models import Gallery
from photos.models import Photo
 
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
 


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'name', 'filename', 'created')

    def picture(self, photo):
        return '<img src= "%s" height="100px" />' % photo.filename.url
    picture.allow_tags = True

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Gallery, GalleryAdmin)


