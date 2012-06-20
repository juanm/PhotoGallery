from django.http import HttpResponse
from models import Gallery
  
def gallery(request, gallery_id):
    mygallery = Gallery.objects.get(id=gallery_id)
    return HttpResponse(mygallery.name + "<br />" + mygallery.description)

