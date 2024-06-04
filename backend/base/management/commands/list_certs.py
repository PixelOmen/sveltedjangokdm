from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ...models import Cert

class Command(BaseCommand):
    help = 'View Users'

    def handle(self, *args, **kwargs):
        certs = Cert.objects.all()
        for cert in certs:
            self.stdout.write(f"id: {cert.id}, file: {cert.file}, url: {cert.file.url}") # type: ignore