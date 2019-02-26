"""DigitalMarketPlace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
from django.conf import settings

# from products.views import create_view
# from products.views import detail_view
# from products.views import detail_slug_view
# from products.views import list_view
# from products.views import update_view
# from products.views import ProductListView
# from products.views import ProductDetailView
# from products.views import ProductCreateView
# from products.views import ProductUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
