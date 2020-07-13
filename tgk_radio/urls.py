from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from radio_main import views
from tgk_radio import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('post_ajax_req', views.put_picture, name='put_picture')
]