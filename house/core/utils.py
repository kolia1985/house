from tddspry.django.cases import HttpTestCase
from django.db import models
from django import forms
from core.widgets import CurrencyWidget, DateInputWithDatepicker


class MockHttpCase(HttpTestCase):
    def fill_values(self, form, data):
        for k, v in data.iteritems():
            self.fv(form, k, v)

    def submitform200(self, form, data):
        self.fill_values(form, data)
        self.submit200()

    def assert_contains(self, message, container):
        count = ("%s" % container).count(message)
        self.assert_false(count==0,
            '"%s" not in """%s"""' % (message, container))

    def assert_not_contains(self, message, container):
        count = ("%s" % container).count(message)
        self.assert_true(count==0, 
            '"%s" find %s in """%s"""' % (message, count, container))

    def assert_count_contains(self, message, container, count):
        count_res = ("%s" % container).count(message)
        self.assert_true(count==count_res, 
            '"%s" find %s of %s in """%s"""' % (
            message, count_res, count, container))

class DateFormField(forms.DateField):
    widget = DateInputWithDatepicker


class DateField(models.DateField):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': DateFormField,
            'required': not self.null,
        }
        defaults.update(kwargs)
        return super(DateField, self).formfield(**defaults)



class DateTimeField(models.DateTimeField):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': DateFormField,
            'required': not self.null,
        }
        defaults.update(kwargs)
        return super(DateTimeField, self).formfield(**defaults) 


class CurrencyFormField(forms.DecimalField):
    widget = CurrencyWidget


class CurrencyField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] =  8
        kwargs['decimal_places'] = 2
        super(CurrencyField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'max_digits': self.max_digits,
            'decimal_places': self.decimal_places,
            'form_class': CurrencyFormField,
            'required': not self.null,
        }
        defaults.update(kwargs)
        return super(CurrencyField, self).formfield(**defaults) 

def choice_value(key, choices):
    for choice in choices:
        if key == choice[0]:
            return choice[1]