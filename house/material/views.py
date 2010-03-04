from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from material.models import WallingMaterial, Armature
from sortedtable.models import AjaxTable

def material_list(request, template='material/material_list.html'):
    """
    material_list list page
    """
    wallingmaterial_list = WallingMaterial.objects.all()
    fields = (("name", "name", ""), 
              ("cost", "cost by m^3", ""),
              ("volume", _("Volume m^3"), ""), )
    wallingmaterial_table = AjaxTable(wallingmaterial_list, fields)
    armature_list = Armature.objects.all()
    fields = (("name", "name", ""), 
              ("cost", "cost by T", ""),
              ("diameter", _("Diameter mm"), ""), )
    armature_table = AjaxTable(armature_list, fields)
    context = RequestContext(request, {"wallingmaterial_table": wallingmaterial_table.render(request),
                                       "armature_table": armature_table.render(request), })
    return render_to_response(template, context)


