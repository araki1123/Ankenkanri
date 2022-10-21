from asyncio.windows_events import NULL
import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from django import setup
setup()

from first_app.models import AnkenList
# AnkenList.objects.create(
a = AnkenList(
    
    keiriShonin= True,
    statusCode= 20,
    status= '案件無効状態',
    edabanGroup= 1,
    shiharaiPattern= 0,
    kanriNo= 'S22-070',
    edaban= 0,
    ankenMei= '無効案件てすと',
    torihikisakiCode= 100002,
    torihikisakiMei= 'ミツイワ㈱',





































    dataKoshinbi= '2022-10-05 20:55:12.146166',

    shainNo= '90001',
    tantosha= '伊豆猛',

    hyojijun= 48














































)

a.save(force_insert=True)