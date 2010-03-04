from django.db import models
from django.utils.translation import ugettext as _
from core.utils import CurrencyField


class Material(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    cost = CurrencyField(_('Cost'))
    density = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        abstract = True

"""
--- = Materials Meta classes = ---
"""

class RectangularMaterial(Material):
    height = models.FloatField(_('Height'))
    width = models.FloatField(_('width'))
    length = models.FloatField(_('length'))

    @property
    def volume(self):
        return self.height * self.width * self.length * 0.000000001

    class Meta:
        abstract = True


class LengthyMaterial(Material):
    """
    TODO: kolia!
    """
    pass

    class Meta:
        abstract = True


class BulkMaterial(Material):
    class Meta:
        abstract = True

"""
--- = Materials Models = ---
"""
class WallingMaterialType(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    def __unicode__(self):
        return u"%s" % self.name


class WallingMaterial(RectangularMaterial):
    type = models.ForeignKey(WallingMaterialType)
    conductivity = models.FloatField(_('Conductivity'), 
                                     null=True, blank=True)



class SlurryMaterialType(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    def __unicode__(self):
        return u"%s" % self.name

class SlurryMaterial(Material):
    type = models.ForeignKey(SlurryMaterialType)


class Armature(LengthyMaterial):
    diameter = models.FloatField()


class Wood(Material):
    pass


class Beam(Wood):
    
    pass

