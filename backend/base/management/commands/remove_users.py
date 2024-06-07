from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'View Users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            user.delete()