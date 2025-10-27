from django.urls import path
from .views import Home, CertificatesIndex, CertificateDetail, CoursesIndex, CourseDetail

# __________________________________________________________________________________________________________________________


urlpatterns = [

    path('', Home.as_view(), name='home'),


    path('api/certificates/', CertificatesIndex.as_view(), name='cert_index'),
    path('api/certificates/<int:cert_id>/', CertificateDetail.as_view(), name='cert_detail'),

   
    path('api/courses/', CoursesIndex.as_view(), name='course_index'),
    path('api/courses/<int:course_id>/', CourseDetail.as_view(), name='course_detail'),

]
