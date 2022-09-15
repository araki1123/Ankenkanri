from django.urls import path
from.import views


app_name = 'first_app'

urlpatterns = [
    # path('hello', views.index, name='index'),
    path('index',views.index,name='index'),
    path('home',views.home,name='home'),
    path('sample',views.sample,name='sample'),
    path('sample3',views.sample3,name='sample3'),
    path('import',views.dataimport,name='import'),
    path('export',views.dataexport,name='export'),
    path('export2',views.export2,name='export2'),
    path('import2',views.import2,name='import2'),
    path('edit',views.edit,name='edit'),
    path('edit2',views.edit2,name='edit2'),
    path('edit3',views.edit3,name='edit3'),
    # path('import3',views.import3,name='import3'),
]