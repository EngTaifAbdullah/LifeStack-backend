from rest_framework import serializers
from .models import Category, Certificate, Course, PersonalDocument

# _____________________________________________________________________________________________________

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

# _____________________________________________________________________________________________________

class certificateSerializer(serializers.ModelSerializer):

    file = serializers.FileField(required=False, allow_null=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # read-only

    class Meta:
        model = Certificate
        fields = '__all__'

# _____________________________________________________________________________________________________


class CourseSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.category_type', read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Course
        fields = ['id', 'title', 'provider', 'description', 'user', 'category', 'category_name']

# _____________________________________________________________________________________________________

class PersonalDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalDocument
        fields = '__all__'

# _____________________________________________________________________________________________________

