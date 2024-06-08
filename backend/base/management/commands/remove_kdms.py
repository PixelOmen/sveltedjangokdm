from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ...models import KDM

class Command(BaseCommand):
    help = 'View Users'

    def handle(self, *args, **kwargs):
        kdms = KDM.objects.all()
        for kdm in kdms:
            kdm.delete()