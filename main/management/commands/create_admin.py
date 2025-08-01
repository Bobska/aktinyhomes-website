import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction


class Command(BaseCommand):
    help = 'Create admin user for production deployment'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # Check if admin user already exists
                if User.objects.filter(username='admin').exists():
                    user = User.objects.get(username='admin')
                    user.set_password('admin123')
                    user.is_superuser = True
                    user.is_staff = True
                    user.save()
                    self.stdout.write(self.style.SUCCESS('Admin user password updated!'))
                else:
                    # Create new admin user
                    User.objects.create_superuser(
                        username='admin',
                        email='admin@aktinyhomes.com',
                        password='admin123'
                    )
                    self.stdout.write(self.style.SUCCESS('Admin user created successfully!'))
                
                self.stdout.write(f'Username: admin')
                self.stdout.write(f'Password: admin123')
                self.stdout.write(f'Email: admin@aktinyhomes.com')
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating admin user: {str(e)}'))
            # Don't fail the entire build process
            self.stdout.write(self.style.WARNING('Continuing with deployment...'))
