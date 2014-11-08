from django.db import models

# Create your models here.
from django.utils import timezone
import uuid
from django.utils.encoding import smart_text


class Place(models.Model):
    uuid = models.CharField(max_length=32)
    venue_uid = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    lat = models.FloatField()
    lng = models.FloatField()

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    outlet_yes = models.IntegerField(default=0)
    outlet_no = models.IntegerField(default=0)

    def has_outlets(self):
        return self.outlet_yes - self.outlet_no

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4().hex

        super(Place, self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_text(self.name)

    @models.permalink
    def get_absolute_url(self):
        return 'place_detail', [self.uuid]

    @models.permalink
    def get_outlet_yes_url(self):
        return 'place_outlet_update', [self.uuid, '+']

    @models.permalink
    def get_outlet_no_url(self):
        return 'place_outlet_update', [self.uuid, '-']


class Comment(models.Model):
    place = models.ForeignKey(Place)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']




