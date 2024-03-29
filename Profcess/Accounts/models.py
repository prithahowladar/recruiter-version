from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class UserInfo(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    college = models.CharField(max_length = 1024, verbose_name = "Name of the College")
    mobile = models.CharField(max_length = 10, verbose_name = "Mobile Number")
    achievemennts = models.TextField(max_length = 1024, verbose_name = "Personal Achievements")
    profile = models.TextField(max_length = 1024, verbose_name = "Preferred Job Profile")
    cgpa = models.FloatField(verbose_name = "CGPA (0.00 - 10.00)", validators = [MaxValueValidator(10), MinValueValidator(0)], default = 0)
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "userinfo")
    branch = models.CharField(max_length = 255)
    email = models.EmailField(null = True)



