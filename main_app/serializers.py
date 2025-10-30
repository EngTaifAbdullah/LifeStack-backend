from rest_framework import serializers
from .models import Category, Certificate, Course, PersonalDocument

# _________________________________________________________

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

# _________________________________________________________

class certificateSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Certificate
        fields = '__all__'

# _________________________________________________________


class CourseSerializer(serializers.ModelSerializer):
    # للقراءة فقط: اسم التصنيف
    category_name = serializers.CharField(source='category.category_type', read_only=True)
    # للكتابة: id التصنيف
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Course
        fields = ['id', 'title', 'provider', 'description', 'user', 'category', 'category_name']
# _________________________________________________________

class PersonalDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalDocument
        fields = '__all__'

# _________________________________________________________

