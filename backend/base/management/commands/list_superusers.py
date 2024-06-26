from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'View Users'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_superuser=True)
        for user in users:
            self.stdout.write(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Date Joined: {user.date_joined}") #type: ignore