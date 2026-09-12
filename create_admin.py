import os
import sys
import django

# Add the project root to sys.path
sys.path.append(os.getcwd())

# 1. Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from django.contrib.auth import get_user_model

def create_admin():
    # 3. Get user model
    User = get_user_model()

    # 4. Check/Create user
    username = 'admin'
    email = 'admin@impulsoshop.com'
    password = 'admin'
    role = 'ADMIN'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            role=role,
            is_staff=True,
            is_superuser=True
        )
        print(f"Superusuario '{username}' creado exitosamente.")
    else:
        print(f"El superusuario '{username}' ya existe.")

if __name__ == '__main__':
    create_admin()
