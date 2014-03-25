from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=200)
    date_pub = models.DateTimeField('date published')
    contents = models.TextField(blank=True)

    def __unicode__(self):
        return self.name