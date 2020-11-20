"""la_estampa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.authtoken import views

from status.urls import urls as status_urls

from account.api import AccountHybridRouter
from creation.api import CreationHybridRouter
from games.hash.api import HashHybridRouter
from contrib.router import HybridRouter

router = HybridRouter()
router.register_router(AccountHybridRouter)
router.register_router(CreationHybridRouter)
router.register_router(HashHybridRouter)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/status/', include((status_urls, 'status'), namespace='status')),

    path('api/', include((router.urls, 'api'), namespace='api'), name='api-root'),
    path('api-token-auth/', views.obtain_auth_token),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
