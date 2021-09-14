from django.db import models

# Create your models here.
from django.db import models
from uuid import uuid4
import uuid


class Users(models.Model):

    uniqueId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    firstName = models.CharField(max_length=50)
    lastName =  models.CharField(max_length=50,blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isVerified = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    class Meta:
        db_table = "users"
