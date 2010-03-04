from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from sortedtable.forms import TableForm


class Table(object):
    """
    Represents table of queryset objects
    """
    template_table = "sortedtable/table.html"
    template_paging = "sortedtable/paging.html"
    template_per_page = "sortedtable/per_page.html"

    def __init__(self, queryset, fields, template_table=None):
        self._model = queryset.model
        self._obj_list = queryset
        self._fields = fields
        self._page = 1
        self._per_page = 10
        self._order_by = ["id", ]
        self.context = None
        if template_table:
            self.template_table = template_table 

    def filter(self, *args, **kwargs):
        self._obj_list = self._obj_list.filter(*args, **kwargs)

    def order_by(self, *args, **kwargs):
        self._obj_list = self._obj_list.order_by(*args, **kwargs)

    def _apply_paging(self, obj_list, page, per_page):
        paginator = Paginator(obj_list, per_page)
        try:
            return paginator.page(page)
        except (EmptyPage, InvalidPage):
            return paginator.page(paginator.num_pages)

    def process_data(self, request):
        if request.method == "POST":   
            table_form = TableForm(request.POST)
            if table_form.is_valid():
                self._page = table_form.cleaned_data["page"]
                self._per_page =  int(table_form.cleaned_data["per_page"])
                self._order_by = table_form.cleaned_data["order_by"]
                if self._order_by:
                    self._order_by = self._order_by.split(",")
                else:
                    self._order_by = []
        else:
            table_form = TableForm()
        return table_form

    def prepare_context(self, request):
        #TODO: Refactore this method. Use inline functions for example.
        table_form = self.process_data(request)
        self.order_by(*self._order_by)
        paginator = self._apply_paging(self._obj_list, \
                                       self._page, self._per_page)
        obj_list = [] 
        for item in paginator.object_list:
            fields = []
            for field in self._fields:
                value = item
                for f in field[0].split("__"):
                    value = getattr(value, f)
                fields.append(value)
            obj_list.append((fields, item, ))

        self._model_fields = []
        for field in self._fields:
            # FIXME: Refactor this code, please
            #_field = self._model._meta.get_field_by_name(\
            #                                field[0].split("__")[0])
            self._model_fields.append(("",
                                       field[2] in self._order_by, \
                                       field[1],
                                       field[2]))

        context = {"obj_list": obj_list, \
                   "fields": self._model_fields, \
                   "paginator": paginator, \
                   "table_form": table_form, \
                   "ordr_by": self._order_by, }
        context = self.update_context(context, paginator.object_list)
        return context

    def update_context(self, context, object_list):
        """
        Method to override
        """
        return context

    def render(self, request, template_table=None):
        context = self.prepare_context(request)
        template = template_table or self.template_table
        return { "table": render_to_string(template, context),
                 "paging": render_to_string(self.template_paging, context),
                 "per_page": render_to_string(self.template_per_page, context) }


class AjaxTable(Table):
    """
    Ajax table with paging, sorting and filtering.
    """
    ajax_template = "sortedtable/ajax_table.html"

    def ajax_render(self, request):
        context = self.prepare_context(request)
        extra_context = {"table_template": self.template_table,
                   "paging_template": self.template_paging, }
        context.update(extra_context)
        return render_to_response(self.ajax_template, context)
