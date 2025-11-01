from django.db import models
from django.contrib.auth.models import User


# ______________________________________________________________________________________________________________

# Add Category like: Task | Cource | Exam

class Category(models.Model):

    CATEGORY_CHOICES = [

        ('Task', 'Task'),
        ('Course', 'Course'),
        ('Exam', 'Exam'),
    ]

    category_type = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='COURSE')

    def __str__(self):
        return self.category_type
    
# ______________________________________________________________________________________________________________

# when you want to uplode your Certificate this is the fields you need to fill out.

class Certificate(models.Model):

    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date_obtained = models.DateField()
    file = models.FileField(upload_to='certificate/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificate')


    def __str__(self):
        return f"{self.title} - {self.organization}"
    
# ______________________________________________________________________________________________________________


class Course(models.Model):

    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')

    def __str__(self):
        return f"{self.title} - {self.provider}"
    


# ______________________________________________________________________________________________________________

# Personal doucument such as: ID | Pasport | Resume

class PersonalDocument(models.Model):

    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='personal_docs/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_docs')

    def __str__(self):
        return self.title
    
# ________________________________________________________________________________________________________________________________________________________________________________________________
