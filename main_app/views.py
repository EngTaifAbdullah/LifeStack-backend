from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Certificate, Course, PersonalDocument, Category
from .serializers import certificateSerializer, CourseSerializer, PersonalDocumentSerializer, CategorySerializer

from django.contrib.auth import get_user_model
from rest_framework.permissions import ( AllowAny, IsAuthenticated, )
from rest_framework_simplejwt.tokens import RefreshToken

# ________________________________________________________________________________________________________________________________________________________________________________________________

User = get_user_model()

class Home(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Welcome to LifeStack App 🍓🌺 "})


# ________________________________________________________________________________________________________________________________________________________________________________________________

# Certificate CRUD (( Read | Create ))

class CertificateIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):    # Read All certificate List

        queryset = Certificate.objects.filter(user=request.user)
        serializer = certificateSerializer(queryset, many=True)
        return Response(serializer.data)

# _____________

    def post(self, request):   # Create new certificate

        serializer = certificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # set owner

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ________________________________________________________________________________________________________________________________________________________________________________________________

# certificate CRUD (( Read | Update | Delete ))

class CertificateDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, cert_id):    # Read spesifice certificate
        obj = get_object_or_404(Certificate, id=cert_id)
        return obj


    def get(self, request, cert_id):
        certificate = self.get_object(cert_id)
        if certificate.user != request.user:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = certificateSerializer(certificate)
        return Response(serializer.data)

# _____________

    def put(self, request, cert_id):   # Update spesifice certificate

        certificate = self.get_object(cert_id)
        if certificate.user != request.user:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = certificateSerializer(certificate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # user unchanged

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# _____________

    def delete(self, request, cert_id):    # Delete spesifice certificate

        certificate = self.get_object(cert_id)
        if certificate.user != request.user:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        certificate.delete()
        return Response({"message": f"Certificate {cert_id} deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

# ________________________________________________________________________________________________________________________________________________________________________________________________

# Courses CRUD (( Read | Create )) $ Courses: filter by user & set owner on create

class CoursesIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):   # Read All Courses List

        queryset = Course.objects.filter(user=request.user)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

# _____________

    def post(self, request):   # Create new Courses

        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ________________________________________________________________________________________________________________________________________________________________________________________________

# Courses CRUD (( Read | Update | Delete ))

class CourseDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, course_id):   # Read spesifice course

        return get_object_or_404(Course, id=course_id)
    def get(self, request, course_id):
        course = self.get_object(course_id)

        if course.user != request.user:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

# _____________

    def put(self, request, course_id):   # Update spesifice course

        course = self.get_object(course_id)
        if course.user != request.user:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# _____________

    def delete(self, request, course_id):   # Delete spesifice course

        course = self.get_object(course_id)
        if course.user != request.user:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        course.delete()
        return Response({"message": f"Course {course_id} deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

# ________________________________________________________________________________________________________________________________________________________________________________________________

# Personal Document CRUD (( Read | Create ))

class PersonalDocsIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):   # Read All Personal Documents List

        queryset = PersonalDocument.objects.filter(user=request.user)
        serializer = PersonalDocumentSerializer(queryset, many=True)
        return Response(serializer.data)

# _____________

    def post(self, request):   # Create new Personal Document

        serializer = PersonalDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ________________________________________________________________________________________________________________________________________________________________________________________________

# Personal Document CRUD (( Read | Update | Delete ))

class PersonalDocDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, doc_id):   # Read spesifice Personal Document

        return get_object_or_404(PersonalDocument, id=doc_id)

    def get(self, request, doc_id):
        doc = self.get_object(doc_id)
        if doc.user != request.user:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonalDocumentSerializer(doc)
        return Response(serializer.data)

# _____________

    def put(self, request, doc_id):   # Update spesifice Personal Document

        doc = self.get_object(doc_id)
        if doc.user != request.user:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PersonalDocumentSerializer(doc, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# _____________

    def delete(self, request, doc_id):   # Delete spesifice Personal Document

        doc = self.get_object(doc_id)
        if doc.user != request.user:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        doc.delete()
        return Response({"message": f"Document {doc_id} deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

# ________________________________________________________________________________________________________________________________________________________________________________________________

# To display it as Drop dowen list

class CategoryList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
# ________________________________________________________________________________________________________________________________________________________________________________________________

# Signup /Sign in / logout Setting

class SignupUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):   # To create new user 

        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")


        if not username or not password or not email:
            return Response({"error": "Please provide a username, password, and email"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': "User Already Exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"id": user.id, "username": user.username, "email": user.email}, status=status.HTTP_201_CREATED)

# ________________________________________________________________________________________________________________________________________________________________________________________________


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):   # To logout

        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)

# ________________________________________________________________________________________________________________________________________________________________________________________________













