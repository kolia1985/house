from django.db import models
from django.utils.translation import ugettext as _


class Foundation(models.Model):
    name = models.CharField(_('Name'), max_length=100)
