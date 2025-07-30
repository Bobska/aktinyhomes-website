#!/usr/bin/env python3
"""
Simple script to create admin user that can be run directly in Render shell
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aktinyhomes.settings')
django.setup()

from django.contrib.auth.models import User

try:
    if User.objects.filter(username='admin').exists():
        user = User.objects.get(username='admin')
        user.set_password('admin123')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print("✓ Admin user password updated!")
    else:
        User.objects.create_superuser(
            username='admin',
            email='admin@aktinyhomes.com',
            password='admin123'
        )
        print("✓ Admin user created successfully!")
    
    print("Username: admin")
    print("Password: admin123")
    print("Email: admin@aktinyhomes.com")
    print("\nYou can now access the admin at: /admin")
    
except Exception as e:
    print(f"✗ Error creating admin user: {str(e)}")
    sys.exit(1)
