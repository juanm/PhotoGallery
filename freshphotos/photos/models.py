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

    VISIBLE_BY_CHOICES = (
        (u'AD', u'Admin'),
        (u'LI', u'Logged In Users'),
        (u'EV', u'Everybody'),
    )

    name = models.CharField(max_length=200)
    filename = models.FileField(upload_to='photos/')
    created = models.DateTimeField(auto_now_add=True)
    galleries = models.ManyToManyField('photos.Gallery')
    visible_by = models.CharField(max_length=2, choices=VISIBLE_BY_CHOICES, default=u'AD')

    class Meta:
        verbose_name_plural  = 'photos'

    def __unicode__(self):
        return self.name
