from asyncio.windows_events import NULL
import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from django import setup
setup()

from first_app.models import AnkenList
# AnkenList.objects.create(
a = AnkenList(
    
    keiriShonin= True,
    statusCode= 0,
    status= '案件入力（作成中）',
    edabanGroup= 3,
    shiharaiPattern= 3,
    kanriNo= 'S22-009',
    edaban= 21,
    ankenMei= 'モバイルPCレンタル月額費用　9月',
    torihikisakiCode= 100003,
    torihikisakiMei= 'ソフトバンク㈱',
    kanjokamoku= '資本準備金',






    mitsumoriLink= 'https://advantec-group.ent.box.com/file/925364524384、https://advantec-group.ent.box.com/file/925858622263',



    ringishoNo= '2022-0654',
    ringishoLink= 'https://advantec-group.ent.box.com/file/925364706508',
    wfNo= '稟議-2022-0654',
    keiyakuKingaku= 3260510,
    keiyakushoNo= '2270-059204',
    keiyakushoLink= 'https://…',

    onatsuRingiLink= 'https://…',



    chumonLink= 'https://…',
    nohinKigen= '2022-10-1 00:00',
    kenshuKigen= '2022-11-30 00:00',
    shiharaiKigen= '2022-12-28 00:00',



    nohinLink= 'https://…',



    seikyushoLink= 'https://…',
    keikaku_Jisseki= 99999999,

    konyuKaisha= 'TRK',
    dataKoshinbi= '2022-9-9 00:00',
    saishuKoshinsha= '荒木',
    shainNo= '12345',
    tantosha= '市ノ川',
    comment= '・・・・',
    hyojijun= 22










































)

a.save(force_insert=True)