import os

from numpy import true_divide

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from django import setup
setup()

from first_app.models import AnkenList

AnkenList.objects.filter(ankenMei='LCM').delete()
