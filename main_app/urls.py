from django.urls import path
from .views import Home, CertificatesIndex, CertificateDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),

  
    path('api/certificates/', CertificatesIndex.as_view(), name='cert_index'),
    path('api/certificates/<int:cert_id>/', CertificateDetail.as_view(), name='cert_detail'),


]
