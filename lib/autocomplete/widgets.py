from django import forms
from django.core.urlresolvers import NoReverseMatch, reverse
from django.template import loader
from django.utils import simplejson
from django.utils.safestring import mark_safe


__all__ = ('AutoCompleteWidget', )


class AutoCompleteWidget(forms.TextInput):

    class Media:
        css = {
            'screen,projection,tv': ('css/jquery.autocomplete.css', )
        }
        js = (
            #'js/jquery-1.3.2.min.js',
            'js/jquery.autocomplete.min.js',
        )

    def __init__(self, *args, **kwargs):
        self.channel = kwargs.pop('channel', None)
        self.options = kwargs.pop('options', {})
        self.choices = list(kwargs.pop('choices', () ))
        self.choice = None
        self.prefix = ""
        related_fields = kwargs.pop('related_fields', None)
        super(AutoCompleteWidget, self).__init__(*args, **kwargs)
        
        if related_fields:
            extra = {}
            if isinstance(related_fields, str):
                related_fields = list(related_fields)

            for field in related_fields:
                extra[field] = "%s_value" % field

            self.extra = extra
        else:
            self.extra = {}
    
    def set_prefix(self, prefix):
        self.prefix = prefix + "-"

    def render(self, name, value, attrs=None):
        channel = getattr(self, 'channel', None)
        help_text = getattr(self, 'help_text', u'')
        options = getattr(self, 'options', {})
        
        self.defaults = {
            'minChars': 3,
            'selectFirst': False,
        }
        self.defaults.update(options)
        
        if self.defaults or self.extra:
            if 'extraParams' in self.defaults:
                self.defaults['extraParams'].update(self.extra)
            else:
                self.defaults['extraParams'] = self.extra

            options = simplejson.dumps(self.defaults, indent=4, sort_keys=True)
            extra = []

            for k, v in self.extra.items():
                options = options.replace(simplejson.dumps(v), v)
                extra.append(u"function %s() { return $('#id_%s%s').val(); }\n" % (v, self.prefix, k))

            extra = u''.join(extra)
        else:
            extra, options = '', ''


        if not channel:
            raise TypeError, 'Please, supply "channel" attribute first.'

        if attrs is not None:
            html_id = attrs.get('id', name)
        else:
            html_id = name


        if isinstance(channel, basestring):
            url = reverse(channel)
        elif isinstance(channel, (list, tuple)):
            url = reverse(*channel)
        else:
            raise TypeError, 'Channel can be only "string" or "list" instance.'

        context = {
            'help_text': help_text,

            'html': super(AutoCompleteWidget, self).render(name, self.choice or value, attrs),
            'html_id': html_id,
            'value': self.choice or value,
            'value_pk': value.pk if hasattr(value, "pk") else value,
            'name': name,
            'js_name': name.replace('-', '_'),
            'options': mark_safe(options),
            'extra': mark_safe(extra),
            'url': url,
        }

        safe_url = url.replace('/', '').replace('autocomplete', '')
        templates = ('autocomplete/autocomplete_%s.html' % safe_url,
                     'autocomplete/autocomplete.html')

        return mark_safe(loader.render_to_string(templates, context))
    
    def set_current_choice(self, data):
        self.choice = data
                
            
    def value_from_datadict(self, data, files, name):
        if not self.choices:
            return super(AutoCompleteWidget, self).value_from_datadict(data, \
                                                                       files, \
                                                                       name)
        if name + "_text" in data:
            self.set_current_choice(data[name + "_text"])
        else:
            self.set_current_choice(data[name])
        return data[name]
