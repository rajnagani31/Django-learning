from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="Create a new user"

    def add_arguments(self,parser):
        parser.add_argument("username", type=str ,help="Username of the new user")
        parser.add_argument("email",type=str,help="Email of the new user")
        parser.add_argument('password',type=str ,help="Password for the new user")

    def handle(self, *args, **kwargs):
        username=kwargs['username']
        email=kwargs['email']
        password=kwargs['password']


        try:
            User.objects.create_user(username=username,email=email,password=password)
            self.stdout.write(self.style.SUCCESS(f" User {username} is created "))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f" ERROR :{e.message_dict}")) 

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"ERROR :{str(e)}"))       