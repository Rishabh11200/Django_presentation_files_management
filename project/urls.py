from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index),
    path('home/',views.home),
    path('login/',views.login),
    path('main/',views.main),
    path('register/',views.register),
    path('cecform/',views.cecform),
    path('profile/',views.profile),
    path('logout/',views.logout),
    path('displayteam/',views.displayteam),
    path('upload/',views.upload),
    path('contact/',views.contact),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
