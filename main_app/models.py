from django.db import models
from django.contrib.auth.models import User


# ______________________________________________________________________________________________________________

# Add Category like: Task | Cource | Exam

class Category(models.Model):
    category_type = models.CharField(max_length=100)

    def __str__(self):
        return self.category_type
    
# ______________________________________________________________________________________________________________

# when you want to uplode your Certificate this is the fields you need to fill out.

class Certificate(models.Model):

    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date_obtained = models.DateField()
    file = models.FileField(upload_to='certificates/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')

    def __str__(self):
        return f"{self.title} - {self.organization}"
    
# ______________________________________________________________________________________________________________


class Course(models.Model):

    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')

    def __str__(self):
        return self.title
