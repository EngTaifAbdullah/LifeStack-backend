from rest_framework import serializers
from .models import Category, Certificate, Course

# _________________________________________________________

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

# _________________________________________________________

class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = '__all__'

# _________________________________________________________

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        
# _________________________________________________________