from django import template
from django.template import Library
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.forms import BaseForm
from report.forms import ReportForm


register = Library()

TEMPLATE = 'core/templatetags/fields.html'
MODELS_TEMPLATE = 'core/templatetags/model_fields.html'
MODEL_TEMPLATE = 'core/templatetags/model_field.html'
REPORT_TEMPLATE = 'core/templatetags/report_fields.html'

@register.tag
def render_fields(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tokens = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, ""

    # Pop tag name
    tokens.pop(0)

    obj = tokens.pop(0)
    fields = tokens

    return FieldsNode(obj, fields)

class FieldsNode(template.Node):
    def __init__(self, obj, fields):
        self.obj = template.Variable(obj)
        self.fields = fields

    def render(self, context):
        obj = self.obj.resolve(context)
        if isinstance(obj, ReportForm):
            return self._render_reportform_fields(obj)
        elif isinstance(obj, BaseForm):
            return self._render_form_fields(obj)
        else:
            return self._render_model_fields(obj)

    def _render_form_fields(self, form):
        if self.fields:
            fields = []
            for field in self.fields:
                field = field.strip('"\'')
                field = form[field]
                fields.append(field)
        else:
            fields = form
        return render_to_string(TEMPLATE, {'fields': fields})

    def _render_reportform_fields(self, form):
        if self.fields:
            fields = []
            for field_name in self.fields:
                val_field = None
                val_min_field = None
                val_max_field = None
                field_name = field_name.strip('"\'')
                field = form[field_name]
                if field.field.display_type == 1:
                    val_field = form[field_name+"_val"]
                elif field.field.display_type == 2:
                     val_min_field = form[field_name+"_val_min"]
                     val_max_field = form[field_name+"_val_max"]
                fields.append((field, val_field, val_min_field, val_max_field, ))
        else:
            fields = form
        return render_to_string(REPORT_TEMPLATE, {'fields': fields,
                                                  'val_field': val_field,
                                                  'val_min_field': val_min_field,
                                                  'val_max_field': val_max_field, })

    def _render_model_fields(self, model):
        from django.db.models.fields import FieldDoesNotExist
        labeled_values = []
        for field_name in self.fields:
            try:
                field = model._meta.get_field_by_name(field_name)[0]
                label = field.verbose_name
            except FieldDoesNotExist:
                label = ' '
            value = getattr(model, field_name)
            if not value:
                value = ''
            if type(value) == bool:
                if value:
                    value = _('Yes')
                else:
                    value = _('No')
            labeled_values.append((label, value))
        context = {'labeled_values': labeled_values, }
        return render_to_string(MODELS_TEMPLATE, context)


@register.inclusion_tag(MODEL_TEMPLATE, takes_context=False)
def render_field(label, value):
    return {'label': _(label), 'value': value, }
