from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    phone_number =  models.CharField(max_length=25)
    # not the best name for prise en charge du client
    onboarding_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name