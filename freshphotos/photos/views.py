from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from models import Gallery
from models import Photo
  
def gallery(request, gallery_id):
    try:
        gallery = Gallery.objects.get(id=gallery_id)
    except Gallery.DoesNotExist:
        raise Http404
    context = {'gallery': gallery}
    return render(request, "gallery.html", context)

def photo(request, photo_id):
    try:
        photo = Photo.objects.get(id=photo_id)
    except Photo.DoesNotExist:
        raise Http404

    context = {'photo': photo}

    return render(request, "photo.html", context)


