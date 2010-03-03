from django.db import models
from django.utils.translation import ugettext as _


class Roof(models.Model):
    """
    Rafter system and cover material.
    """
    name = models.CharField(_('Name'), max_length=100)
