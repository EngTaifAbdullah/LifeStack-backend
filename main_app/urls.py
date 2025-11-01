from django.urls import path
from .views import ( Home, CertificateIndex, CertificateDetail, CoursesIndex, CourseDetail, PersonalDocsIndex, PersonalDocDetail, CategoryList, SignupUserView, LogoutView )
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# ________________________________________________________________________________________________________________________________________________________________________________________________

urlpatterns = [

    path('', Home.as_view(), name='home'),


    path('certificate/', CertificateIndex.as_view(), name='certificate_index'),
    path('certificate/<int:cert_id>/', CertificateDetail.as_view(), name='certificate_detail'),


    path('courses/', CoursesIndex.as_view(), name='course_index'),
    path('courses/<int:course_id>/', CourseDetail.as_view(), name='course_detail'),


    path('personal/', PersonalDocsIndex.as_view(), name='personal_index'),
    path('personal/<int:doc_id>/', PersonalDocDetail.as_view(), name='personal_detail'),


    path('categories/', CategoryList.as_view(), name='categories'),


    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]
# ________________________________________________________________________________________________________________________________________________________________________________________________