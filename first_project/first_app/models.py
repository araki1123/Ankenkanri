from django.db import models

# Create your models here.
class AnkenList(models.Model):
    keiriShonin = models.BooleanField(null=True,blank=True)
    statusCord = models.IntegerField(null=True,blank=True)
    status = models.CharField(null=True,blank=True,max_length=30)
    edabanGroup = models.IntegerField(null=True,blank=True)
    shiharaiPattern = models.IntegerField(null=True,blank=True)
    kanriNo = models.CharField(null=True,blank=True,max_length=30)
    edaban = models.CharField(null=True,blank=True,max_length=30)
    ankenMei = models.CharField(null=True,blank=True,max_length=30)
    torihikisakiCode = models.IntegerField(null=True,blank=True)
    torihikisakiMei = models.CharField(null=True,blank=True,max_length=30)
    kanjokamoku = models.CharField(null=True,blank=True,max_length=30)
    keikakuTanka = models.IntegerField(null=True,blank=True)
    keikakuSuu = models.IntegerField(null=True,blank=True)
    keikakuGokei = models.IntegerField(null=True,blank=True)
    mitsumoriTanka = models.IntegerField(null=True,blank=True)
    mitsumoriSuu = models.IntegerField(null=True,blank=True)
    mitsumoriGokei = models.IntegerField(null=True,blank=True)
    mtsumoriLink = models.URLField(null=True,blank=True)
    wfNo = models.CharField(null=True,blank=True,max_length=30)
    keiyakuKingaku = models.IntegerField(null=True,blank=True)
    chumonTanka = models.IntegerField(null=True,blank=True)
    chumonSuu = models.IntegerField(null=True,blank=True)
    chumonGokei = models.IntegerField(null=True,blank=True)
    chumonLink = models.URLField(null=True,blank=True)
    nohinTanka = models.IntegerField(null=True,blank=True)
    nohinSuu = models.IntegerField(null=True,blank=True)
    nohinGokei = models.IntegerField(null=True,blank=True)
    shiharaiTanka = models.IntegerField(null=True,blank=True)
    konyuSuu = models.IntegerField(null=True,blank=True)
    konyuGokei = models.IntegerField(null=True,blank=True)
    seikyushoLink = models.URLField(null=True,blank=True)
    keikaku_Jisseki = models.IntegerField(null=True,blank=True)
    nohinKigen = models.DateTimeField(null=True,blank=True)
    kenshuKigen = models.DateTimeField(null=True,blank=True)
    shiharaiKigen = models.DateTimeField(null=True,blank=True)
    kurikaeshiKigen = models.DateTimeField(null=True,blank=True)
    ringishoLink = models.URLField(null=True,blank=True)
    keiyakushoLink = models.URLField(null=True,blank=True)
    konyuKaisha = models.CharField(null=True,blank=True,max_length=30)
    dataKoshinbi = models.DateTimeField(null=True,blank=True)
    saishuKoshinsha = models.CharField(null=True,blank=True,max_length=30)
    shainNo = models.IntegerField(null=True,blank=True)
    tantosha = models.CharField(null=True,blank=True,max_length=30)
    comment = models.CharField(null=True,blank=True,max_length=30)


    class Meta:
        db_table = 'ankenListTable'
        
    def __str__(self):
        return f'{self.ankenMei}'        