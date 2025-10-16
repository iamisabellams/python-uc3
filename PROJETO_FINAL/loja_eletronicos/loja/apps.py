from django.apps import AppConfig


class LojaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loja'


class SiteLojaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_loja'

    def ready(self):
        import site_loja.signals # Importa o arquivo de signals