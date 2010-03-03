from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from core.models import Building

def home(request, template='core/index.html'):
    """
    Home page
    """
    #building = Building.objects.get(pk=1)
    building = None
    context = RequestContext(request, {"building": building, })
    return render_to_response(template, context)

def project(request, project_slug, template='core/project.html'):
    building = get_object_or_404(Building, slug=project_slug)
    context = RequestContext(request, {"building": building, })
    return render_to_response(template, context)
