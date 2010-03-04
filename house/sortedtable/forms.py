from django import forms
from django.utils.translation import ugettext as _


class TableForm(forms.Form):
    PER_PAGE_CHOICES = ((10, 10), (20, 20), (50, 50))
    per_page = forms.ChoiceField(initial=10, label=_('View per page'), 
                                 choices=PER_PAGE_CHOICES, )
    page = forms.IntegerField(initial=1, min_value=1, widget=forms.HiddenInput)
    order_by = forms.CharField(initial="id", widget=forms.HiddenInput)
