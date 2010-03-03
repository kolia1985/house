from django.template import Library

register = Library()


@register.inclusion_tag('core/templatetags/static.html', takes_context=True)
def static(context, section):
    context.update({'section': section})
    return context

@register.inclusion_tag('core/templatetags/js.html', takes_context=True)
def js(context, file):
    context.update({'file': file})
    return context

@register.inclusion_tag('core/templatetags/css.html', takes_context=True)
def css(context, file, media=None):
    context.update({
        'file': file,
        'media': media
    })
    return context
