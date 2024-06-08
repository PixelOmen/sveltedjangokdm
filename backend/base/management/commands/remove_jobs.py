from django.core.management.base import BaseCommand
from ...models import Job

class Command(BaseCommand):
    help = 'View jobs'

    def handle(self, *args, **kwargs):
        jobs = Job.objects.all()
        for job in jobs:
            job.delete()