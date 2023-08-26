from django.contrib import admin
from django.urls import path
from myapp1.views import home_page, get_settings, get_state, send_message, send_file_by_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_settings'),
    path('get_settings/', get_settings, name='get_settings'),
    path('get_state/', get_state, name='get_state'),
    path('send_message/', send_message, name='send_message'),
    path('send_file_by_url/', send_file_by_url, name='send_file_by_url')
]



