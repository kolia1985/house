from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from core.models import Building, Floor
from sortedtable.models import AjaxTable

def home(request, template='core/index.html'):
    """
    Home page
    """
    building_list = Building.objects.all()
    fields = (("name", "name", ""),
              ("width", "width", ""),
              ("length", "length", ""),
              ("square", "square", ""), )
    table = AjaxTable(building_list, fields,'core/project_table.html' )
    context = RequestContext(request, {"building_table": table.render(request), })
    return render_to_response(template, context)

def project(request, project_slug, template='core/project.html'):
    building = get_object_or_404(Building, slug=project_slug)
    fields = (("name", "name", ""),
              ("height", "height", ""),
              ("square", "square", "")
               )
    floor_table = AjaxTable(building.floors.all(), fields,'core/project_table.html' )
    context = RequestContext(request, {"building": building,
                                       "floor_table": floor_table.render(request),})
    return render_to_response(template, context)

def floor(request, id, template='core/floor.html'):
    floor = get_object_or_404(Floor, pk=id)
    context = RequestContext(request, {"floor": floor,})
    return render_to_response(template, context)
