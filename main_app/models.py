from django.db import models
from django.contrib.auth.models import User


# ______________________________________________________________________________________________________________

# Create your models here.

# add catogory like: Task,Cource,Exam

class Category(models.Model):
    category_type = models.CharField(max_length=100)

    def __str__(self):
        return self.category_type