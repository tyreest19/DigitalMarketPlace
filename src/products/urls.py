from django.contrib import admin
from django.urls import path
from .views import create_view
from .views import detail_view
from .views import detail_slug_view
from .views import list_view
from .views import update_view
from .views import ProductListView
from .views import ProductDetailView
from .views import ProductCreateView
from .views import ProductUpdateView
from .views import ProductDownloadView

urlpatterns = [
    path('add/', ProductCreateView.as_view(), name='create_view'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail_view'),
    path('detail/<int:pk>/edit/', ProductDetailView.as_view()),
    path('list/', ProductListView.as_view(), name='list_view'),
]
