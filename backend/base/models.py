from django.db import models
from django.contrib.auth.models import User

class Cert(models.Model):
    file = models.FileField(upload_to='certs/')
    display_name = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
    class Meta:
        ordering = ['-file']

    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = self.file.name
        super(Cert, self).save(*args, **kwargs)

class DKDM(models.Model):
    file = models.FileField(upload_to='dkdms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
    class Meta:
        ordering = ['-file']