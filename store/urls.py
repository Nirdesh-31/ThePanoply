from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Leave as empty string for base url
    path('', views.index, name="index"),
    path('product/', views.product, name="product"),
    path('about/', views.about, name="about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
