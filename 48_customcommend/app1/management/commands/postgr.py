from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand,CommandError
from django.core.validators import validate_email
from django.db import connections
from django.core.management import call_command

class Command(BaseCommand):
    help='Run Postgreas SQL'


    def handle(self, *args, **options):
        db="custom"
        try:
            # post_db=connections['custom']

            # self.stdout.write(self.style.SUCCESS("Your DB conneact successfully"))

            self.stdout.write(self.style.NOTICE("Makin migrations..."))
            call_command('makemigrations')

            self.stdout.write(self.style.NOTICE(f'Migrating to "{db}"...'))
            call_command('migrate', database=db)    

            self.stdout.write(self.style.SUCCESS(f"Successfully migrated to {db}"))
        
        # except Exception:
        #     self.stdout.write(self.style.ERROR("Your db doesn't conneact"))  

        except Exception as e:
            raise CommandError(f'Error during migration: {e}')