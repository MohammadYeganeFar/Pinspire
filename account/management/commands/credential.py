from django.core.management.base import BaseCommand, CommandError
import base64
from account.models import CustomUser


import time
from hashlib import md5
from config import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    help = "Returns a jwt token"

    def add_arguments(self, parser):
        parser.add_argument("id", type=int)
        parser.add_argument("email", type=str)

    def handle(self, *args, **options):
        user_id = options['id']
        user_email = options['email']
        user = User.objects.filter(id=user_id, email=user_email).exists()

        if not user:
            raise CommandError(
                f"User with id {user_id} and email {user_email} not found")

        t = int(time.time())
        string_to_sign = str(user_id) + settings.SECRET_KEY + str(t) + "Maktab126"

        sign = md5(string_to_sign.encode('utf-8')).hexdigest()

        token = f"{user_id}:{sign}:{t}"

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created token: {token}')
        )

