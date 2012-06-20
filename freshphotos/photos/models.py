from django.db import models

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural  = 'galleries'

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=200)
    filename = models.FileField(upload_to='photos/')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural  = 'photos'

    def __unicode__(self):
        return self.name
