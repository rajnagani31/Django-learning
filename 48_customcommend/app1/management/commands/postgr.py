from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core.validators import validate_email
from django.db import connections
from django.core.management import call_command

class Command(BaseCommand):
    help='Run Postgreas SQL'

    def handle(self, *args, **options):
        try:
            post_db=connections['custom']
            self.stdout.write(self.style.SUCCESS("Your DB conneact successfully"))
        
        except Exception:
            self.stdout.write(self.style.ERROR("Your db doesn't conneact"))  