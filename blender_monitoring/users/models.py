from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('doctor', 'Médico'),
        ('technician', 'Técnico'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    # Evita los conflictos de accesores inversos
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
    )
