from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    help = 'Ensures the demo user exists with the correct permissions'

    def handle(self, *args, **options):
        demo_username = 'demo_user'
        demo_email = 'demo@example.com'
        demo_password = 'demopass123'  # In a real app, use environment variables

        user, created = User.objects.get_or_create(
            username=demo_username,
            defaults={
                'email': demo_email,
                'is_active': True,
                'is_staff': True  # Give staff access for demo purposes
            }
        )

        if created:
            user.set_password(demo_password)
            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created demo user'))
        else:
            # Ensure the password is correct if the user already exists
            if not user.check_password(demo_password):
                user.set_password(demo_password)
                user.save()
                self.stdout.write(self.style.SUCCESS('Updated demo user password'))
            else:
                self.stdout.write('Demo user already exists')
