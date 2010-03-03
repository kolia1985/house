from django.db import models
from django.utils.translation import ugettext as _
from roof.models import Roof
from foundation.models import Foundation
from wall.models import Wall


class Floor(models.Model):
    FLOOR_TYPE = ((1, _('Basement')), 
                  (2, _('Ground')),
                  (3, _('Common')),
                  (4, _('Attic')),
                  (5, _('Attic 2')), )
    name = models.CharField(_('Name'), max_length=100)
    type = models.IntegerField(choices=FLOOR_TYPE)
    wall = models.ManyToManyField(Wall, through='FloorWall')
    height = models.FloatField()

    def unicode(self):
        return u"%s" % self.name
    # overlay
    # floor
    # ceiling


class FloorWall(models.Model):
    floor = models.ForeignKey(Floor)
    wall = models.ForeignKey(Wall)
    length = models.FloatField()


class Building(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'))
    foundation = models.ForeignKey(Foundation, null=True, blank=True)
    floors = models.ManyToManyField(Floor)
    roof = models.ManyToManyField(Roof, null=True, blank=True)
    width = models.FloatField()
    length = models.FloatField()

    def unicode(self):
        return u"%s" % self.name
