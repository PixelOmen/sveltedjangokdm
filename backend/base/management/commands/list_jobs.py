from django.core.management.base import BaseCommand
from ...models import Job

class Command(BaseCommand):
    help = 'View jobs'

    def handle(self, *args, **kwargs):
        jobs = Job.objects.all()
        for job in jobs:
            self.stdout.write(f"ID: {job.id}, Cert: {job.cert.display_name}, DKDM: {job.dkdm.display_name}, User: {job.user.username}, Created At: {job.created_at}, Completed At: {job.completed_at}, Status: {job.status}, Error: {job.error}")