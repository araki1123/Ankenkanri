from django import forms
from django.core import validators
from .models import AnkenList

class formAnkenList(forms.ModelForm):



        
    keiriShonin = forms.BooleanField(label='経理承認',required=False)
    # statusCode = forms.IntegerField(label='ステータスコード',required=False)
    statusCode = forms.ChoiceField(label='ステータスコード',choices=(
        (0,'案件入力（作成中）'),
        (1,'案件入力（完成）'),
        (2,'見積書（作成依頼）'),
        (3,'見積書（入手済み）'),
        (4,'稟議書（承認完了）'),
        (5,'契約書（作成完了）'),
        (6,'契約書（締結完了）'),
        (7,'注文処理（完了）'),
        (8,'納品（完了）'),
        (9,'請求書（入手済み）'),
        (10,'支払処理（完了）'),
        (20,'案件無効状態'),
        (99,'親案件用')
    ))
    status = forms.CharField(label='案件ステータス',required=False)
    # status = forms.ChoiceField(label='案件ステータス',choices=(
    #     (0,'案件入力（作成中）'),
    #     (1,'案件入力（完成）'),
    #     (2,'見積書（作成依頼）'),
    #     (3,'見積書（入手済み）'),
    #     (4,'稟議書（承認完了）'),
    #     (5,'契約書（作成完了）'),
    #     (6,'契約書（締結完了）'),
    #     (7,'注文処理（完了）'),
    #     (8,'納品（完了）'),
    #     (9,'請求書（入手済み）'),
    #     (10,'支払処理（完了）')
    # ))
    edabanGroup = forms.IntegerField(label='枝番グループ',required=False)
    # shiharaiPattern = forms.IntegerField(label='支払パターン',required=False)
    shiharaiPattern = forms.ChoiceField(label='支払パターン',choices=(
        (0,'1回の支払いで完了'),
        (1,'繰り返し（月1回）、終了期限あり'),
        (2,'繰り返し（月1回）、終了期限なし'),
        (3,'繰り返し（年1回）、終了期限あり'),
        (4,'繰り返し（年1回）、終了期限なし'),
    ))
    kanriNo = forms.CharField(label='管理No.')
    edaban = forms.CharField(label='枝番')
    ankenMei = forms.CharField(label='案件名',max_length=100)
    # torihikisakiCode = forms.IntegerField(label='取引先コード',required=False)
    torihikisakiCode = forms.ChoiceField(label='取引先コード',choices=(
        (100001,'富士通JAPAN㈱'),
        (100002,'ミツイワ㈱'),
        (100003,'ソフトバンク㈱'),
        (100004,'㈱大塚商会'),
        (100005,'リコージャパン㈱'),
        (100006,'日立システムズ'),
        (100007,'三菱UFJリサーチ＆コンサルティング㈱'),
        (100008,'コムテック㈱'),
        (100009,'キャノンマーケティングジャパン㈱'),
        (100010,'GMOグローバルサインHD㈱'),
        (100000,'')
    ))
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
    # shainNo = forms.IntegerField(label='社員番号',required=False)
    shainNo = forms.ChoiceField(label='社員番号',choices=(
        (90001,'伊豆猛'),
        (18083,'長田秀行'),
        (99003,'志田慶介'),
        (17048,'市ノ川弘彰'),
        (4023,'八木原暁宣'),
        (99005,'平原道高'),
        (17059,'荒木歩'),
    ))
    tantosha = forms.CharField(label='担当者名',required=False)
    comment = forms.CharField(label='コメント',required=False)
    hyojijun = forms.IntegerField(label='表示順',required=False)

 
    class Meta:
        model = AnkenList
        fields = '__all__'

    # def __init__(self,*args,**kwargs):
    #     self.request = kwargs.pop("request")
    #     super (formAnkenList,self).__init__(*args,**kwargs)
        