from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import HttpResponse, HttpResponseForbidden, \
                        HttpResponseNotFound, HttpResponseServerError, \
                        QueryDict
from django.template import RequestContext, loader
from django.utils import simplejson
from django.utils.encoding import force_unicode, smart_str
from django.utils.translation import ugettext as _


AUTOCOMPLETE_PRETTIFY = getattr(settings, 'AUTOCOMPLETE_PRETTIFY', {})
AUTOCOMPLETE_RELATED_FIELDS = getattr(settings, \
                                      'AUTOCOMPLETE_RELATED_FIELDS', {})

def autocomplete(request, app_label, model):
    try:
        content_type = ContentType.objects.get(app_label=app_label,
                                               model=model)
    except ContentType.DoesNotExist:
        return HttpResponse(u'', mimetype='text/plain')

    try:
        exclude = request.GET.getlist('exclude')
    except KeyError:
        exclude = ()
    else:
        exclude = dict([(smart_str(k), v) \
                        for k, v in QueryDict('&'.join(exclude)).items()])

    try:
        fields = request.GET.getlist('fields')
    except KeyError:
        fields = ()

    try:
        order_by = request.GET.getlist('order_by')
    except KeyError:
        order_by = ()
        
    related_fields = AUTOCOMPLETE_RELATED_FIELDS.get('%s.%s' % \
                                                     (app_label, model), None)

    query = None
    if related_fields:
        for field in  related_fields:
            value = request.GET.get(field, None)
            if value:
                q = Q(**{smart_str('%s' % field): value})
                if query is None:
                    query = q
                else:
                    query = query | q

    prettify = AUTOCOMPLETE_PRETTIFY.get('%s.%s' % (app_label, model), None)
    
    value = request.GET.get('q', '')
    for field in fields:
        
        q = Q(**{smart_str('%s__icontains' % field): value})
        if query is None:
            query = q
        else:
            query = query | q

    objects = content_type.model_class().objects

    if query:
        objects = objects.filter(query)
    else:
        objects = objects.all()

    if exclude:
        objects = objects.exclude(**exclude)

    if order_by:
        objects = objects.order_by(*order_by)

    response = []

    for obj in objects:
        prettified = prettify and prettify(obj) or force_unicode(obj)
        result = ('%d' % obj.pk,
                  force_unicode(obj),
                  prettified)
        response.append('|'.join(result))

    return HttpResponse('\n'.join(response), mimetype='text/plain')
