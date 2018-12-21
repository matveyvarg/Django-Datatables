from django import template
from django_datatables.tables import Table
register = template.Library()


@register.inclusion_tag(filename="table.html", takes_context=True)
def render_table(context, table: Table = None):
    if not table:
        table = context['datatable']
    return {'table': table}


@register.inclusion_tag(filename="static.html", takes_context=True)
def render_static(context, table: Table = None):
    if not table:
        table = context['datatable']

    # set style of table:

    return {'table': table}
