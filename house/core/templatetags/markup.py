from django.template import Library
from django.utils.translation import ugettext as _

register = Library()


@register.inclusion_tag('core/templatetags/accordion-header.html', 
                        takes_context=False)
def acc_header(title, css_class="", text="", url=""):
    return {"title": _(title),
            "css_class": css_class, 
            "text": text.replace("{{ title }}", title),
            "url": url, }
