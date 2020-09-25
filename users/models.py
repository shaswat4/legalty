from django.db import models

# Create your models here.



class account(models.Model):

    username =  models.CharField( max_length = 20 )
    password =  models.CharField( max_length = 30 )
    is_lawyer = models.BooleanField( default= False )