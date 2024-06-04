from django.db import models
from django.contrib.auth.models import User

class Cert(models.Model):
    file = models.FileField(upload_to='certs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
    class Meta:
        ordering = ['-file']

class DKDM(models.Model):
    file = models.FileField(upload_to='dkdms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
    class Meta:
        ordering = ['-file']