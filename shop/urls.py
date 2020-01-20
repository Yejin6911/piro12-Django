from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')


app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
    path('', views.item_list),
    path('<int:pk>/', views.item_detail),
    #장고 1버전
    #re_path(r'^(?P<pk>\d+)/$',views.item_detail),
]