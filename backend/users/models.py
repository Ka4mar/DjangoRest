from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
