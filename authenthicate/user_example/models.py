from django.db import models

# Create your models here.

class userPhone(models.Model):
    ''' Add password OR a way to authenticate '''
    user = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 12)

    def __str__(self):
        return "username: {} - phone: {}".format(self.user, self.phone)
