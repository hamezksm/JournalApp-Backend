from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    choices =(
        ('male','male'),
        ('female','female'),
        ('non-binary','non-binary'),
    )
    
    # Add any additional fields that you need for you user account
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=choices)
    
class Journal(models.Model):
    user = models.ForeignKey(User, related_name='journals', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
 