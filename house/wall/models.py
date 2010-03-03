from django.db import models
from django.utils.translation import ugettext as _
from material.models import WallingMaterial, SlurryMaterial, Armature


class Window(models.Model):
    height = models.FloatField(_('Height'))
    width = models.FloatField(_('width'))
    length = models.FloatField(_('length'))
    name = models.CharField(_('Name'), max_length=100)

    def unicode(self):
        return u"%s" % self.name

class DoorWay(models.Model):
    height = models.FloatField(_('Height'))
    width = models.FloatField(_('width'))
    length = models.FloatField(_('length'))
    name = models.CharField(_('Name'), max_length=100)

    def unicode(self):
        return u"%s" % self.name

class Door(models.Model):
    height = models.FloatField(_('Height'))
    width = models.FloatField(_('width'))
    length = models.FloatField(_('length'))
    name = models.CharField(_('Name'), max_length=100)

    def unicode(self):
        return u"%s" % self.name

class Jumper(models.Model):
    height = models.FloatField(_('Height'))
    width = models.FloatField(_('width'))
    length = models.FloatField(_('length'))
    slurry_material = models.ForeignKey(SlurryMaterial)
    main_armature = models.ForeignKey(Armature, related_name="main_jumper")
    length_main_armature = models.FloatField()
    extra_armature = models.ForeignKey(Armature, null=True, blank=True, 
                                       related_name="extra_jumper")
    length_extra_armature = models.FloatField(null=True, blank=True)

    def unicode(self):
        return u"%s" % self.length

class WallType(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    walling_material = models.ManyToManyField(WallingMaterial, through='WallMaterial')

    def unicode(self):
        return u"%s" % self.name


class Wall(models.Model):
    name = models.CharField(_('Name'), max_length=100, null=True, blank=True)
    type = models.ForeignKey(WallType)
    windows = models.ManyToManyField(Window, through='WallWindow', null=True, blank=True)
    doors = models.ManyToManyField(Door, through='WallDoor', null=True, blank=True)
    door_ways = models.ManyToManyField(DoorWay, through='WallDoorWay', null=True, blank=True)

    def unicode(self):
        return u"%s" % self.name


class WallMaterial(models.Model):
    wall = models.ForeignKey(WallType)
    material = models.ForeignKey(WallingMaterial)
    volume = models.FloatField(null=True, blank=True)
    slurry_material = models.ForeignKey(SlurryMaterial)

class WallWindow(models.Model):
    wall = models.ForeignKey(Wall)
    window = models.ForeignKey(Window)
    jamper = models.ForeignKey(Jumper, null=True, blank=True)

class WallDoor(models.Model):
    wall = models.ForeignKey(Wall)
    window = models.ForeignKey(Door)
    jamper = models.ForeignKey(Jumper, null=True, blank=True)

class WallDoorWay(models.Model):
    wall = models.ForeignKey(Wall)
    window = models.ForeignKey(DoorWay)
    jamper = models.ForeignKey(Jumper, null=True, blank=True)
