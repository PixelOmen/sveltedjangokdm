from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'View Users'

    def handle(self, *args, **kwargs):
        User.objects.create_user(username='TestUser')