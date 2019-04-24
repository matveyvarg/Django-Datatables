DJANGO DATATABLES PACKAGE
#########################
Easy way to implement datatables to your django application

Installation
************

    pip install  django-datatables

Add app to *INSTALLED_APPS*

.. code-block:: python

    INSTALLED_APPS = (
        'django.contrib.contenttypes',
        'django.contrib.staticfiles',
         ...
        'django_datatables',
    )


Usage
*****

At first, you need to load template tags to your template:

.. code-block:: html

    {% load table_tags %}

Then render static files:

.. code-block:: html

    {% render_static %}

After that you need to import **Table** class from **django_datatables.tables**.
Then, we must create instance of table with specified params and pass this instance to **datatable** variable.
And call template tag to render the table

.. code-block:: html

    {% render_table  %}

Example:

.. code-block:: python

    from django.views.generic import
    from django_datatables.tables import Table

    class IndexView(TemplateView):

        template_name = 'index.html'

        def get_context_data(self, **kwargs):
            context = super(IndexView, self).get_context_data()
            context['datatable'] = Table(User.objects.all(), ['email', 'id'], load_jquery=True, style=Table.STYLE_FOUNDATION)
            return context

.. code-block:: html

    {% load table_tags %}
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        {% render_static %}
    </head>
    <body>
        {% render_table %}
    </body>
    </html>

Also you can provide table instance right to templte tag:

.. code-block:: html

    {% render_table table %}


Notes
*****

Current version doesn't support Relation fields and FileField