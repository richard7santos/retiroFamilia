
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user_profile import urls as user_urls
from subscription import urls as subscription_urls

from core.views import home, userLogout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', userLogout, name='logout'),
    path('user/', include(user_urls)),
    path('inscricao/', include(subscription_urls)),

    path('', home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
