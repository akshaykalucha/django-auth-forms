from django.db import models  

class Contact(models.Model):
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=1030)

    def __str__(self):
        return self.email