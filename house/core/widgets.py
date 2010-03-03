from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import get_template, Context


class DateInputWithDatepicker(forms.DateInput):
    """
    Date widget with JQuery UI Datepicker
    """
    class Media:
        js =  ('core/datepicker.js', )

    def render(self, name, value, attrs=None):
        """
        Render widget
        """
        attrs["class"] = 'datefield'
        output = super(DateInputWithDatepicker, self).render(name, \
                                                             value, attrs)
        template = get_template("core/widgets/datepicker.html")
        context = Context({"name": name, })
        init_script = template.render(context)
        output = output + init_script
        return mark_safe(output)


class DateHiddentWidget(forms.HiddenInput):
    """
    Hidden field with JQuery UI Datepicker
    """
    class Media:
        js =  ('core/datepicker.js', )

    def render(self, name, value, attrs=None):
        field = super(DateHiddentWidget, self).render(name, value, attrs)
        template = get_template("core/widgets/hidden_datepicker.html")
        context = Context({"name": name, 'value': value, 'field': field, })
        output = template.render(context)
        return mark_safe(output)


class CurrencyWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        attrs["class"] = 'currencyfield'
        input = super(CurrencyWidget, self).render(name, value, attrs)
        template = get_template("core/widgets/currency.html")
        context = Context({"input": input, })
        output = template.render(context)
        return mark_safe(output)
