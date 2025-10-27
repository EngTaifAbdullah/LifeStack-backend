from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Certificate, Course, PersonalDocument
from .serializers import CertificateSerializer, CourseSerializer, PersonalDocumentSerializer

# __________________________________________________________________________________________________________________________

class Home(APIView):
    
    def get(self, request):
        return Response({"message": "Welcome to LifeStack App 🍓🌺 "})


    def post(self, request):
        data = request.data
        return Response({
            "message": "You just posted to LifeStack",
            "data": data
        })
# __________________________________________________________________________________________________________________________


# Certificates CRUD (( Read | Create ))

class CertificatesIndex(APIView):

    def get(self, request):  # Read All certificates List

        queryset = Certificate.objects.all()
        serializer = CertificateSerializer(queryset, many=True)

        return Response(serializer.data)



    def post(self, request):  # Create new certificate

        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ____________________________________

# Certificates CRUD (( Read | Update | Delete ))

class CertificateDetail(APIView):

    def get(self, request, cert_id):  # Read spesifice certificates

        certificate = get_object_or_404(Certificate, id=cert_id)
        serializer = CertificateSerializer(certificate)

        return Response(serializer.data)



    def put(self, request, cert_id):  # Update spesifice certificates

        certificate = get_object_or_404(Certificate, id=cert_id)
        serializer = CertificateSerializer(certificate, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, cert_id):  # Delete spesifice certificates
        
        certificate = get_object_or_404(Certificate, id=cert_id)
        certificate.delete()

        return Response({"message": f"Certificate {cert_id} deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

# __________________________________________________________________________________________________________________________

# Courses CRUD (( Read | Create ))

class CoursesIndex(APIView):

    def get(self, request):  # Read All Courses List

        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)

        return Response(serializer.data)



    def post(self, request): # Create new Courses

        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ____________________________________

# Courses CRUD (( Read | Update | Delete ))

class CourseDetail(APIView):   

    def get(self, request, course_id):  # Read spesifice course

        course = get_object_or_404(Course, id=course_id)
        serializer = CourseSerializer(course)

        return Response(serializer.data)



    def put(self, request, course_id):  # Update spesifice course

        course = get_object_or_404(Course, id=course_id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 

    def delete(self, request, course_id):  # Delete spesifice course

        course = get_object_or_404(Course, id=course_id)
        course.delete()

        return Response({"message": f"Course {course_id} deleted"}, status=status.HTTP_204_NO_CONTENT)

# __________________________________________________________________________________________________________________________

# Personal Document CRUD (( Read | Create ))

class PersonalDocsIndex(APIView):

    def get(self, request):  # Read All Personal Document List

        queryset = PersonalDocument.objects.all()
        serializer = PersonalDocumentSerializer(queryset, many=True)

        return Response(serializer.data)











# __________________________________________________________________________________________________________________________