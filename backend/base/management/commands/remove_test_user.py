from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'View Users'

    def handle(self, *args, **kwargs):
        user = User.objects.get(id = 1)
        user.delete()
