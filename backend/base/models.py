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
        ordering = ['-display_name']

    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = self.file.name
        super(Cert, self).save(*args, **kwargs)

class DKDM(models.Model):
    file = models.FileField(upload_to='dkdms/')
    display_name = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
    class Meta:
        ordering = ['-display_name']

    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = self.file.name
        super(DKDM, self).save(*args, **kwargs)

class KDM(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='kdms/')
    display_name = models.CharField(max_length=512, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
    class Meta:
        ordering = ['-display_name']

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    cert = models.ForeignKey(Cert, on_delete=models.CASCADE)
    dkdm = models.ForeignKey(DKDM, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateTimeField(null=True)
    endDate = models.DateTimeField(null=True)
    timezone = models.CharField(max_length=255, null=True)
    outputDir = models.CharField(max_length=512, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=255, default='ok')
    error = models.TextField(null=True)
    kdm = models.ForeignKey(KDM, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id} - {self.created_at} - {self.status}'

    class Meta:
        ordering = ['-created_at']