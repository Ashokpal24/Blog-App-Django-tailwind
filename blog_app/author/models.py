from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField()
    def __str__(self):
        return f"{0}".format(self.user.username)