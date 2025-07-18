import getpass
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core.validators import validate_email

class Command(BaseCommand):

    help="Create a normel user "

    def handle(self, *args, **options):
        username=input(" Username :")
        email=input(" Email:")
        password= getpass.getpass(" Password:")
        password2=getpass.getpass(" Password (again) :")


        if password2 != password:
            self.stdout.write(self.style.ERROR("Password dosen't Matched !"))

            return

        try:
            validate_email(email)
        except ValidationError :
            self.stdout.write(self.style.ERROR("ERROR : Enter a valid email address."))

            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR("ERROR : This user already exists."))

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR("ERROR : This email already exists."))

        try:
            User.objects.create_user(username=username,email=email,password=password)
            self.stdout.write(self.style.SUCCESS(f"User {username} Create Successfully."))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f"ERROR :{e}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"ERROR : {str(e)}"))                        