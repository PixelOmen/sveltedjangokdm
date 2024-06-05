from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ...models import DKDM

class Command(BaseCommand):
    help = 'View Users'

    def handle(self, *args, **kwargs):
        dkdms = DKDM.objects.all()
        for dkdm in dkdms:
            self.stdout.write(f"id: {dkdm.id}, file: {dkdm.file}, display_name: {dkdm.display_name}, url: {dkdm.file.url}, user: {dkdm.user}") # type: ignore