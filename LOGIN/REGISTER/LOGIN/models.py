from django.db import models
from django.contrib.auth.models import User

#Create your models here.
#login & Register Form
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=True)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

# Create your models here.
#Company Information Form

class Company_Info(models.Model):
    Company_Name = models.CharField(max_length=100)
    Company_Address =models.CharField(max_length=300)
    Company_Email= models.EmailField()
    Comapny_Country =models.CharField(max_length=60)
    Comapny_State = models.CharField(max_length=50)
    Company_City= models.CharField(max_length=50)
    Company_Contact =models.CharField(max_length=10)
    Company_Category=models.CharField(max_length=200)


    def __str__(self):
        return self.Company_Name
