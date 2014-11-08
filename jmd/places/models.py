from django.db import models

# Create your models here.
from django.utils import timezone
import uuid
from django.utils.encoding import smart_text


class Category(models.Model):
    name = models.CharField(max_length=120)
    uid = models.CharField(max_length=120)


class Place(models.Model):
    uuid = models.CharField(max_length=32)
    venue_uid = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    lat = models.FloatField()
    lng = models.FloatField()

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4().hex

        super(Place, self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_text(self.name)

    @models.permalink
    def get_absolute_url(self):
        return 'place_detail', [self.uuid]






