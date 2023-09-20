from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class HaikuModel(models.Model):
    title = models.CharField(max_length=225,unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a ForeignKey to User


    def __str__(self):
        return self.title