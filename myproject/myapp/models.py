# from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models 




# Create your models here.


class UserInfo(models.Model):
    country=CountryField(blank=True)

    bio = models.CharField(max_length=500, blank=True, null=True) # Max length of 500 characters

    phone_number = PhoneNumberField(blank=True, null=True) # Optional: blank=True, null=True for non-required fields 

    areas_of_interest = models.TextField(blank=True)

    user_documents= models.FileField(upload_to='documents/')

    birthday = models.DateField(null=True, blank=True)

    location_of_home_address=models.PointField(blank=True, null=True) # Stores longitude and latitude
        # You can also store separate latitude and longitude fields if preferred
        # latitude = models.FloatField(blank=True, null=True)
        # longitude = models.FloatField(blank=True, null=True)

    location_of_office_address=models.PointField(blank=True, null=True)

    image = models.ImageField(upload_to='my_images/') # 'my_images/' is a subdirectory within MEDIA_ROOTge 








    def __str__(self):
        return f"{self.pk} - {self.country}"

    @property
    def age(self):
        if self.birthday:
            from datetime import date
            today = date.today()
            return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return None

    @property
    def is_geo_enabled(self):
        return self.location_of_home_address or self.location_of_office_address




   
 
