from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Get username by user ID'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        try:
            user = User.objects.get(id=user_id)
            self.stdout.write(self.style.SUCCESS(f"Username for user ID {user_id}: {user.username}"))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User with ID {user_id} does not exist"))
