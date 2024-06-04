from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ...models import Cert

class Command(BaseCommand):
    help = 'View Users'

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.get(username="TestUser")
        except User.DoesNotExist:
            print("Test User not found")
            exit()
        cert1 = Cert(user=user, file="certs/cert1.pem")
        cert2 = Cert(user=user, file="certs/cert2.pem")
        cert3 = Cert(user=user, file="certs/cert3.pem")
        cert1.save()
        cert2.save()
        cert3.save()
        print("Certs created successfully")
