import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from django import setup
setup()

from first_app.models import AnkenList
# AnkenList.objects.create(
a = AnkenList(
    
    keiriShonin= True,
    statusCord= 0,
    status= '案件入力（作成中）',
    edabanGroup= 3,
    shiharaiPattern= 3,
    kanriNo= 'S22-010',
    edaban= '1',
    ankenMei= 'Office365 月額費用　4月',
    saishuKoshinsha= '荒木',
    shainNo= 17059,
    tantosha= '荒木',
    comment= '・・・・'



















)

a.save(force_insert=True)