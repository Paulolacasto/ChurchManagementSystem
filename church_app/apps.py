from django.apps import AppConfig

class ChurchAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'church_app'
    verbose_name = "Church Management Application"  # Makes it easier to recognize in Django Admin
