from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Generate_Student_Data, name='Generate_Student_Data'),
    path('covertdata', views.covertdata, name='covertdata'),
    path('sendmail', views.sendmail, name='sendmail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)