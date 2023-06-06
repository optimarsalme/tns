
from django.contrib import admin
from django.urls import path, include
from api import views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', include('portfolio.urls')),
    path('admin', admin.site.urls),
    path('tembea/', include('tembea.urls')),
    
    #path('services', views.servicesList),
    #path('services/<slug:service_title>', views.service),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
