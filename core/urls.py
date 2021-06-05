from django.contrib import admin
from django.urls import conf, path
from django.conf.urls.static import static
from django.conf import settings
from myapp.views import course,link_a

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',course),
    path('<int:id>/details/',link_a)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
