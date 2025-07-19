
import time
from hashlib import md5
from pinspire_project import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    help = "decodes a jwt token"

    def add_arguments(self, parser):
        parser.add_argument("token", type=str)

    def handle(self, *args, **options):
        token = options['token']
        user_id, signature, t = token.split(':')
        current_time = int(time.time())
        diff = abs(current_time - int(t))
        if diff > 3 * 60:
            raise CommandError("Invalid token")

        user = User.objects.filter(id=user_id).exists()

        if not user:
            raise CommandError(
                f"User with id {user_id} not found")

        string_to_sign = str(user_id) + settings.SECRET_KEY + str(t) + "Maktab126"

        sign = md5(string_to_sign.encode('utf-8')).hexdigest()

        if sign != signature:
            raise CommandError("invalid token")

        self.stdout.write(
            self.style.SUCCESS('Successfully logged in')
        )
