
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from products.views import Inicio
from users.views import Login,register,logoutUsuario 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('products.urls')),
    path('',login_required(Inicio.as_view()), name='index'),
    path('accounts/login/',Login.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout', login_required(logoutUsuario), name= 'logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

