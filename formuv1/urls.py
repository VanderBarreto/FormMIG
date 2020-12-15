"""
@author: Vanderlino Coelho Barreto Neto

"""


from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .revista import Revistas
from .revista import Login

login=Login()
revistas=Revistas()

urlpatterns = [

    #path('admin/', admin.site.urls),
    path('login/', login.user_login, name='login'),
    path('revista/', revistas.revista, name='revista'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
@author: Vanderlino Coelho Barreto Neto

"""