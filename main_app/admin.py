from django.contrib import admin
from .models import Certificate, Course, PersonalDocument,Category

# Register your models here.

admin.site.register(Certificate)
admin.site.register(Course)
admin.site.register(PersonalDocument)
admin.site.register(Category)