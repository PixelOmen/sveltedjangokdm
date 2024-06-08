from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ...models import KDM

class Command(BaseCommand):
    help = 'View Users'

    def handle(self, *args, **kwargs):
        kdms = KDM.objects.all()
        for kdm in kdms:
            if kdm.file:
                self.stdout.write(f"id: {kdm.id}, file: {kdm.file}, display_name: {kdm.display_name}, url: {kdm.file.url}, user: {kdm.user}, created_at: {kdm.created_at}")
            else:
                self.stdout.write(f"id: {kdm.id}, file: {kdm.file}, display_name: {kdm.display_name}, url: Doesn't Exist, user: {kdm.user}, created_at: {kdm.created_at}")