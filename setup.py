from setuptools import setup

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(BASE_DIR, 'README.rst')) as f:
    README = f.read()

setup(
    name='django-datatables',
    version='0.1',
    packages=['django_datatables'],
    description='Fast way to implement datatables',
    long_description=README,
    author='Matvei Vargasov',
    author_email='matveyvarg@example.com',
    url='https://github.com/yourname/django-datatables/',
    license='MIT',
    install_requires=[
        'Django>=2.0',
    ]
)
