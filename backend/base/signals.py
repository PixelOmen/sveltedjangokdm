from django.dispatch import receiver
from django.db.models.signals import post_delete

from . import models

@receiver(post_delete, sender=models.Cert)
def cert_delete(sender, instance, **kwargs):
    instance.file.delete(False)

@receiver(post_delete, sender=models.DKDM)
def dkdms_delete(sender, instance, **kwargs):
    instance.file.delete(False)