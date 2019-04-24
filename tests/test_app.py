from random import randint

from django.test import TestCase
from django.contrib.staticfiles import finders
from django.template import Context, Template

from model_mommy import mommy

from django_datatables.tables import Table, EmptyQueryset
from tests.testapp.models import TestModel


class TestApp(TestCase):

    def setUp(self):
        mommy.make(TestModel, _quantity=randint(1, 5), make_m2m=True, _create_files=True)
        self.qs = TestModel.objects.all()
        self.template_to_render = Template(
            """
            {% load table_tags %}
            {% render_table %}
            """
        )

    def test_empty_queryset(self):
        with self.assertRaises(EmptyQueryset):
            table = Table(None)

    def test_default_style(self):
        table = Table(self.qs)

        # CHECK STYLE
        self.assertEqual(table.get_style(), Table.STYLE_BASE)

        # CHECK STATIC FILES
        self.assertIsNotNone(finders.find(table.get_dt_src_css()), table.get_dt_src_css())
        self.assertIsNotNone(finders.find(table.get_src_js()))

        # CHECK RENDER TABLE
        context = Context({'datatable': table})
        rendered_template = self.template_to_render.render(context)
