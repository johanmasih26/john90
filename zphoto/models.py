from django.db import models

# Create your models here.
class photo(models.Model):
    name = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="images")
    date = models.DateTimeField(auto_now_add=True)
    