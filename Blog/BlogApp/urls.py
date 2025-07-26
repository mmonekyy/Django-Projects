from django.contrib import admin
from django.urls import path , include
from .views import recipes , aboutme , recipie
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Recipes',recipes, name="Recipes"),
    path('AboutMe',aboutme),
    path('Recipes/<int:id>',recipie),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)