from asyncio.windows_events import NULL
from pickle import NONE
from re import I
from unittest.mock import NonCallableMock
from django.shortcuts import render
from django.http import HttpResponse
from  .import forms
from django.forms import formset_factory

import sqlite3
import openpyxl
import os
# from numpy import true_divide
# from django import setup
from .models import AnkenList

# Create your views here.

# def index(request):
#     return HttpResponse('<h1> Good Bye </h1>')

def index (request):
    context = {
        'ankenList' : AnkenList.objects.all()
    }
    return render(request,'index.html',context)

def home(request):
    my_name = 'Taro Yamada'
    favourite_fruits = ['Apple','Grape','Lemon']
    my_info = {
        'name': 'Taro',
        'age': 18
    }
    return render(request, 'home.html',context={
        'my_name':my_name,
        'favourite_fruits':favourite_fruits,
        'my_info':my_info,
    })

def sample (request):
    name = 'ichiro yamada'
    height = 175.5
    weight = 72
    bmi = weight / (height /100)**2
    page_url = 'https://www.google.com'
    favourete_fruits = [
        'Apple','Grape','Lemon'
    ]
    msg = """hello
    my name is
    ichiro
    """
    msg2 = '1234567890'
    return render(request, 'sample.html',context = {
        'name':name,
        'bmi' : bmi,
        'page_url':page_url,
        'fruits':favourete_fruits,
        'msg':msg,
        'msg2':msg2
    })

class Country:
    
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

def sample3(request):
    country = Country('Japan', 100000000, 'Tokyo')
    return render(request,'sample3.html',context={
        'country':country
    })
    
def export2 (request):
    inputFile=request.POST.get('inputFile')
    context = {
        'ankenList' : AnkenList.objects.all(),
        'inputFile' : inputFile
    }
    if request.method == "POST":
        if "inputFile" in request.POST:
 
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet['A1'].value = 'id'
            sheet['B1'].value = '経理承認'
            sheet['C1'].value = 'ステータスコード'
            sheet['D1'].value = '案件ステータス'
            sheet['E1'].value = '枝番グループ'
            sheet['F1'].value = '支払パターン'
            sheet['G1'].value = '管理No.'
            sheet['H1'].value = '枝番'
            sheet['I1'].value = '案件名'
            sheet['J1'].value = '取引先コード'
            sheet['K1'].value = '取引先名'
            sheet['L1'].value = '勘定科目'
            sheet['M1'].value = '計画単価'
            sheet['N1'].value = '計画数'
            sheet['O1'].value = '計画合計金額'
            sheet['P1'].value = '見積単価'
            sheet['Q1'].value = '見積数'
            sheet['R1'].value = '見積合計金額'
            sheet['S1'].value = '見積書リンク'
            sheet['T1'].value = '稟議書単価'
            sheet['U1'].value = '稟議書数'
            sheet['V1'].value = '稟議書合計'
            sheet['W1'].value = '稟議書No.'
            sheet['X1'].value = '稟議書リンク'
            sheet['Y1'].value = 'ワークフローNo.'
            sheet['Z1'].value = '契約金額'
            sheet['AA1'].value = '契約書No.'
            sheet['AB1'].value = '契約書リンク'
            sheet['AC1'].value = '押捺稟議No.'
            sheet['AD1'].value = '押捺稟議リンク'
            sheet['AE1'].value = '注文単価'
            sheet['AF1'].value = '注文数'
            sheet['AG1'].value = '注文合計金額'
            sheet['AH1'].value = '注文書リンク'
            sheet['AI1'].value = '納品日期限'
            sheet['AJ1'].value = '検収日期限'
            sheet['AK1'].value = '支払日期限'
            sheet['AL1'].value = '納品単価'
            sheet['AM1'].value = '納品数'
            sheet['AN1'].value = '納品合計金額'
            sheet['AO1'].value = '納品書リンク'
            sheet['AP1'].value = '支払単価'
            sheet['AQ1'].value = '購入数'
            sheet['AR1'].value = '購入合計金額'
            sheet['AS1'].value = '請求書リンク情報'
            sheet['AT1'].value = '計画－実績'
            sheet['AU1'].value = '支払繰返し期限'
            sheet['AV1'].value = '購入会社'
            sheet['AW1'].value = '最終データ更新日'
            sheet['AX1'].value = '最終更新者'
            sheet['AY1'].value = '社員番号'
            sheet['AZ1'].value = '担当者名'
            sheet['BA1'].value = 'コメント'
            sheet['BB1'].value = '表示順'






            db = sqlite3.connect('db.sqlite3')
            c = db.cursor()
            c.execute('SELECT * FROM ankenListTable')
            for i, row in enumerate (c):
                sheet['A' + str(i+2)].value = row[0]
                sheet['B' + str(i+2)].value = row[1]
                sheet['C' + str(i+2)].value = row[2]
                sheet['D' + str(i+2)].value = row[3]
                sheet['E' + str(i+2)].value = row[4]
                sheet['F' + str(i+2)].value = row[5]
                sheet['G' + str(i+2)].value = row[6]
                sheet['H' + str(i+2)].value = row[7]
                sheet['I' + str(i+2)].value = row[8]
                sheet['J' + str(i+2)].value = row[9]
                sheet['K' + str(i+2)].value = row[10]
                sheet['L' + str(i+2)].value = row[11]
                sheet['M' + str(i+2)].value = row[12]
                sheet['N' + str(i+2)].value = row[13]
                sheet['O' + str(i+2)].value = row[14]
                sheet['P' + str(i+2)].value = row[15]
                sheet['Q' + str(i+2)].value = row[16]
                sheet['R' + str(i+2)].value = row[17]
                sheet['S' + str(i+2)].value = row[18]
                sheet['T' + str(i+2)].value = row[19]
                sheet['U' + str(i+2)].value = row[20]
                sheet['V' + str(i+2)].value = row[21]
                sheet['W' + str(i+2)].value = row[22]
                sheet['X' + str(i+2)].value = row[23]
                sheet['Y' + str(i+2)].value = row[24]
                sheet['Z' + str(i+2)].value = row[25]
                sheet['AA' + str(i+2)].value = row[26]
                sheet['AB' + str(i+2)].value = row[27]
                sheet['AC' + str(i+2)].value = row[28]
                sheet['AD' + str(i+2)].value = row[29]
                sheet['AE' + str(i+2)].value = row[30]
                sheet['AF' + str(i+2)].value = row[31]
                sheet['AG' + str(i+2)].value = row[32]
                sheet['AH' + str(i+2)].value = row[33]
                sheet['AI' + str(i+2)].value = row[34]
                sheet['AJ' + str(i+2)].value = row[35]
                sheet['AK' + str(i+2)].value = row[36]
                sheet['AL' + str(i+2)].value = row[37]
                sheet['AM' + str(i+2)].value = row[38]
                sheet['AN' + str(i+2)].value = row[39]
                sheet['AO' + str(i+2)].value = row[40]
                sheet['AP' + str(i+2)].value = row[41]
                sheet['AQ' + str(i+2)].value = row[42]
                sheet['AR' + str(i+2)].value = row[43]
                sheet['AS' + str(i+2)].value = row[44]
                sheet['AT' + str(i+2)].value = row[45]
                sheet['AU' + str(i+2)].value = row[46]
                sheet['AV' + str(i+2)].value = row[47]
                sheet['AW' + str(i+2)].value = row[48]
                sheet['AX' + str(i+2)].value = row[49]
                sheet['AY' + str(i+2)].value = row[50]
                sheet['AZ' + str(i+2)].value = row[51]
                sheet['BA' + str(i+2)].value = row[52]
                sheet['BB' + str(i+2)].value = row[53]


            c.close()
            workbook.save(inputFile) 
 
    
        
    return render(request,'export2.html',context)


        
def dataimport (request):
    context = {
        'ankenList' : AnkenList.objects.all()
    }
    return render(request,'import.html',context)
   
   
def dataexport (request):
    context = {
        'ankenList' : AnkenList.objects.all()
    }
    return render(request,'export.html',context)
     

    
def import2 (request):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
    from django import setup
    setup()
    
    inputFile=request.POST.get('inputFile')
    print('インプットファイルは',inputFile)
    if request.method == "POST":
        if "inputFile" in request.POST:
 
            workbook = openpyxl.load_workbook(inputFile)
            sheet = workbook.active
            it = sheet.iter_rows(min_row=2)
            kanriNos = []
            edabans = []
            for row in it:
                kanriNos.append(row[6].value)
                edabans.append(row[7].value)
                # print('IDの値は',row[0].value)
                # AnkenList.objects.update_or_create (
                ankn, created=AnkenList.objects.update_or_create (    
                    kanriNo= row[6].value,
                    edaban= row[7].value,
                    defaults={
                        "keiriShonin" : row[1].value,
                        "statusCode" : row[2].value,
                        "status" : row[3].value,
                        "edabanGroup" : row[4].value,
                        "shiharaiPattern" : row[5].value,
                        "kanriNo" : row[6].value,
                        "edaban" : row[7].value,
                        "ankenMei" : row[8].value,
                        "torihikisakiCode" : row[9].value,
                        "torihikisakiMei" : row[10].value,
                        "kanjokamoku" : row[11].value,
                        "keikakuTanka" : row[12].value,
                        "keikakuSuu" : row[13].value,
                        "keikakuGokei" : row[14].value,
                        "mitsumoriTanka" : row[15].value,
                        "mitsumoriSuu" : row[16].value,
                        "mitsumoriGokei" : row[17].value,
                        "mitsumoriLink" : row[18].value,
                        "ringiTanka" : row[19].value,
                        "ringiSuu" : row[20].value,
                        "ringiGokei" : row[21].value,
                        "ringishoNo" : row[22].value,
                        "ringishoLink" : row[23].value,
                        "wfNo" : row[24].value,
                        "keiyakuKingaku" : row[25].value,
                        "keiyakushoNo" : row[26].value,
                        "keiyakushoLink" : row[27].value,
                        "onatsuRingiNo" : row[28].value,
                        "onatsuRingiLink" : row[29].value,
                        "chumonTanka" : row[30].value,
                        "chumonSuu" : row[31].value,
                        "chumonGokei" : row[32].value,
                        "chumonLink" : row[33].value,
                        "nohinKigen" : row[34].value,
                        "kenshuKigen" : row[35].value,
                        "shiharaiKigen" : row[36].value,
                        "nohinTanka" : row[37].value,
                        "nohinSuu" : row[38].value,
                        "nohinGokei" : row[39].value,
                        "nohinLink" : row[40].value,
                        "shiharaiTanka" : row[41].value,
                        "konyuSuu" : row[42].value,
                        "konyuGokei" : row[43].value,
                        "seikyushoLink" : row[44].value,
                        "keikaku_Jisseki" : row[45].value,
                        "kurikaeshiKigen" : row[46].value,
                        "konyuKaisha" : row[47].value,
                        "dataKoshinbi" : row[48].value,
                        "saishuKoshinsha" : row[49].value,
                        "shainNo" : row[50].value,
                        "tantosha" : row[51].value,
                        "comment" : row[52].value,
                        "hyojijun" : row[53].value,

                    }    
                )
                

            # print('ＩＤリスト：',ids) 
            ankenList=AnkenList.objects.all()   
            for anken in ankenList:
                hantei=0
                for edabanss in edabans:
                    for kanriNoss in kanriNos:
                        if anken.kanriNo==kanriNoss:
                            if anken.edaban==edabanss:
                                hantei=1
                if hantei==0:
                    AnkenList.objects.filter(id=anken.id).delete()                          

    context = {
        'ankenList' : AnkenList.objects.all(),
        'inputFile' : inputFile
    }            
             
          
    return render(request,'import2.html',context)


def importTest (request):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
    from django import setup
    setup()
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
    a.save()
    context = {
        'ankenList' : AnkenList.objects.all(),
        
    }
    return render(request,'import2.html',context)


def edit(request):
    form = forms.formAnkenList()
    # a=AnkenList.objects.all().count()
    # TestFormset = formset_factory(forms.formAnkenList)
    # formset = TestFormset(request.POST or None)
    # print("ふぉーむせっとは",formset)
    # if formset.is_valid():
    #     formset.save()
        
        # for form in formset:
        #     print(form.cleaned_data)
        
    return render(
        request,'edit.html',context={'form':form,'ankenList' : AnkenList.objects.all()}
    )
    
def edit2(request):
    form = forms.formAnkenList()
    if request.method == 'POST':
        form = forms.formAnkenList(request.POST)
        
    return render(
        request,'edit2.html',context={'form':form,'ankenList' : AnkenList.objects.all()}
    )
    
    
def edit3(request):
    form = forms.formAnkenList()
    print("リクエストメソッドは",request.method)
    print("リクエストポストは",request.POST)
    if request.method == 'POST':
        form = forms.formAnkenList(request.POST)
        print("ふぉーむは",form)
        if form.is_valid():
            form.save()
            # print("ふぉーむせっとは",form.cleaned_data)          
           
    return render(
        request,'edit3.html',context={'form':form,'ankenList' : AnkenList.objects.all()}
    )    