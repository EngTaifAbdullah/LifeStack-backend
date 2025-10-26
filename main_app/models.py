from django.db import models
from django.contrib.auth.models import User


# ______________________________________________________________________________________________________________

# add catogory like: Task,Cource,Exam

class Category(models.Model):
    category_type = models.CharField(max_length=100)

    def __str__(self):
        return self.category_type
    
# ______________________________________________________________________________________________________________
# when you whant to uplode your Certificate this is the must  feild to appliy

class Certificate(models.Model):

    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date_obtained = models.DateField()
    file = models.FileField(upload_to='certificates/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')

    def __str__(self):
        return f"{self.title} - {self.organization}"
    
# ______________________________________________________________________________________________________________
