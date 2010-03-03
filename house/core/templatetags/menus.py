from django.template import Library
from django.utils.translation import ugettext as _
from company.models import CompanyType, Company
from django.core.urlresolvers import reverse

register = Library()


@register.inclusion_tag('core/templatetags/manager_section.html', 
                        takes_context=False)
def manager_menu_item(user):
    context = {"show_item": False, }
    if user.is_authenticated():
        profile = user.get_profile()
        is_admin, company_type = profile.user_role
        if is_admin:
            if company_type.pk == CompanyType.ROA:
                url = reverse('manager_main')
            else:
                company = Company.objects.get_by_type(user.company.slug, 
                                                         company_type) 
                url = company.get_edit_url()
            context.update({"show_item": is_admin, 
                            "title": _('Manager'),
                            "url": url, })
    return context
