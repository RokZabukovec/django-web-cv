from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'download$', views.download_pdf,),
    url(r'^$', views.index, name='index'),
]
