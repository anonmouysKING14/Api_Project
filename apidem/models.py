from django.db import models
class Task(models.Model):
    PhoneNumber=models.CharField(max_length=200)
    Created=models.DateTimeField(auto_now=True)
    Installed= models.BooleanField(default=False,blank=True,null=True)
    class Meta:
        ordering=['-Created']
    def __str__(self):
        return self.title