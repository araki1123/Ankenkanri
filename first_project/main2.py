from asyncio.windows_events import NULL
import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from django import setup
setup()

from first_app.models import AnkenStatus
# AnkenList.objects.create(
a = AnkenStatus(
    
    ankenStatusCode= 10,
    
    ankenStatus = '支払処理(完了）'
)

a.save(force_insert=True)