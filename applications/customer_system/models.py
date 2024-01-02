from django.db import models

class CustomerModel(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    url = models.URLField()
    subscribed = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.name