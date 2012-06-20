from django.db import models

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    best_photo = models.ForeignKey('photos.Photo', blank=True, null=True)

    class Meta:
        verbose_name_plural  = 'galleries'

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=200)
    filename = models.FileField(upload_to='photos/')
    created = models.DateTimeField(auto_now_add=True)
    galleries = models.ManyToManyField('photos.Gallery')

    class Meta:
        verbose_name_plural  = 'photos'

    def __unicode__(self):
        return self.name
