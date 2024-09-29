from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    interests = models.TextField()  # Store interests as text
    bio = models.TextField(blank=True)

    class Meta:
        db_table = 'user_profile'  # Specify the custom table name
