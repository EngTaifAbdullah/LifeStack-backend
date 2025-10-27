from django.urls import path
from .views import Home, CertificatesIndex, CertificateDetail, CoursesIndex, CourseDetail, PersonalDocsIndex, PersonalDocDetail

# __________________________________________________________________________________________________________________________


urlpatterns = [

    path('', Home.as_view(), name='home'),


    path('api/certificates/', CertificatesIndex.as_view(), name='cert_index'),
    path('api/certificates/<int:cert_id>/', CertificateDetail.as_view(), name='cert_detail'),
   

    path('api/courses/', CoursesIndex.as_view(), name='course_index'),
    path('api/courses/<int:course_id>/', CourseDetail.as_view(), name='course_detail'),


    path('api/personal/', PersonalDocsIndex.as_view(), name='personal_index'),
    path('api/personal/<int:doc_id>/', PersonalDocDetail.as_view(), name='personal_detail'),

]
