import os
import urllib
import urllib2
import urlparse
from django.core.files.base import ContentFile
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField('slug')
    date_pub = models.DateTimeField('date published')
    contents = models.TextField(blank=True)
    author = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    img_file = models.ImageField('file name', upload_to='imgs/', blank=True)
    img_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self):
        if self.img_url:
            image_data = urllib2.urlopen(self.img_url, timeout=5)
            filename = urlparse.urlparse(image_data.geturl()).path.split('/')[-1]
            self.img_file = filename
            self.img_file.save(
                filename,
                ContentFile(image_data.read()),
                save=False
            )
        super(News, self).save()
