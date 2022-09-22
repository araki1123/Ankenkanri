from django import forms
from django.core import validators
from .models import AnkenList

class formAnkenList(forms.ModelForm):



        
    keiriShonin = forms.BooleanField(label='経理承認',required=False)
    statusCode = forms.IntegerField(label='ステータスコード',required=False)
    status = forms.CharField(label='案件ステータス',required=False)
    edabanGroup = forms.IntegerField(label='枝番グループ',required=False)
    shiharaiPattern = forms.IntegerField(label='支払パターン',required=False)
    kanriNo = forms.CharField(label='管理No.',required=False)
    edaban = forms.CharField(label='枝番',required=False)
    ankenMei = forms.CharField(label='案件名',required=False,max_length=100)
    torihikisakiCode = forms.IntegerField(label='取引先コード',required=False)
    torihikisakiMei = forms.CharField(label='取引先名',required=False)
    kanjokamoku = forms.CharField(label='勘定科目',required=False)
    keikakuTanka = forms.IntegerField(label='計画単価',required=False)
    keikakuSuu = forms.IntegerField(label='計画数',required=False)
    keikakuGokei = forms.IntegerField(label='計画合計金額',required=False)
    mitsumoriTanka = forms.IntegerField(label='見積単価',required=False)
    mitsumoriSuu = forms.IntegerField(label='見積数',required=False)
    mitsumoriGokei = forms.IntegerField(label='見積合計金額',required=False)
    mitsumoriLink = forms.URLField(label='見積書リンク',required=False)
    ringiTanka = forms.IntegerField(label='稟議書単価',required=False)
    ringiSuu = forms.IntegerField(label='稟議書数',required=False)
    ringiGokei = forms.IntegerField(label='稟議書合計',required=False)
    ringishoNo = forms.CharField(label='稟議書No.',required=False)
    ringishoLink = forms.URLField(label='稟議書リンク',required=False)
    wfNo = forms.CharField(label='ワークフローNo.',required=False)
    keiyakuKingaku = forms.IntegerField(label='契約金額',required=False)
    keiyakushoNo = forms.CharField(label='契約書No.',required=False)
    keiyakushoLink = forms.URLField(label='契約書リンク',required=False)
    onatsuRingiNo = forms.CharField(label='押捺稟議No.',required=False)
    onatsuRingiLink = forms.URLField(label='押捺稟議リンク',required=False)
    chumonTanka = forms.IntegerField(label='注文単価',required=False)
    chumonSuu = forms.IntegerField(label='注文数',required=False)
    chumonGokei = forms.IntegerField(label='注文合計金額',required=False)
    chumonLink = forms.URLField(label='注文書リンク',required=False)
    nohinKigen = forms.DateTimeField(label='納品日期限',required=False)
    kenshuKigen = forms.DateTimeField(label='検収日期限',required=False)
    shiharaiKigen = forms.DateTimeField(label='支払日期限',required=False)
    nohinTanka = forms.IntegerField(label='納品単価',required=False)
    nohinSuu = forms.IntegerField(label='納品数',required=False)
    nohinGokei = forms.IntegerField(label='納品合計金額',required=False)
    nohinLink = forms.URLField(label='納品書リンク',required=False)
    shiharaiTanka = forms.IntegerField(label='支払単価',required=False)
    konyuSuu = forms.IntegerField(label='購入数',required=False)
    konyuGokei = forms.IntegerField(label='購入合計金額',required=False)
    seikyushoLink = forms.URLField(label='請求書リンク情報',required=False)
    keikaku_Jisseki = forms.IntegerField(label='計画－実績',required=False)
    kurikaeshiKigen = forms.DateTimeField(label='支払繰返し期限',required=False)
    konyuKaisha = forms.CharField(label='購入会社',required=False)
    dataKoshinbi = forms.DateTimeField(label='最終データ更新日',required=False)
    saishuKoshinsha = forms.CharField(label='最終更新者',required=False)
    shainNo = forms.IntegerField(label='社員番号',required=False)
    tantosha = forms.CharField(label='担当者名',required=False)
    comment = forms.CharField(label='コメント',required=False)
    hyojijun = forms.IntegerField(label='表示順',required=False)

 
    class Meta:
        model = AnkenList
        fields = '__all__'

    # def __init__(self,*args,**kwargs):
    #     self.request = kwargs.pop("request")
    #     super (formAnkenList,self).__init__(*args,**kwargs)
        