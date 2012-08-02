from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render

from models import Gallery
from models import Photo
from forms import PhotoForm
  
def gallery(request, gallery_id):
    try:
        gallery = Gallery.objects.get(id=gallery_id)
    except Gallery.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.visible_by = 'AD'
            new_photo.save()
            form.save_m2m()
            return HttpResponseRedirect("/gallery/%s/" % gallery_id)
    else:
        form = PhotoForm()
        context = {'gallery': gallery,
               'form' : form}
    
    return render(request, "gallery.html", context)


def photo(request, photo_id):
    try:
        photo = Photo.objects.get(id=photo_id)
    except Photo.DoesNotExist:
        raise Http404

    context = {'photo': photo}

    return render(request, "photo.html", context)


