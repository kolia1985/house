from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from wall.models import WallType
from sortedtable.models import AjaxTable

def wall_type_list(request, template='wall/walltype_list.html'):
    """
    walltype list page
    """
    walltype_list = WallType.objects.all()
    fields = (("name", "name", ""), 
              ("cost", "cost by m^2", ""), )
    table = AjaxTable(walltype_list, fields)
    context = RequestContext(request, {"walltype_table": table.render(request), })
    return render_to_response(template, context)


