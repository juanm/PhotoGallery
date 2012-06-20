from django.http import HttpResponse
from django.shortcuts import render

from models import Gallery
  
def gallery(request, gallery_id):
    gallery = Gallery.objects.get(id=gallery_id)
    context = {'gallery': gallery}
    return render(request, "gallery.html", context)


