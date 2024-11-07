from django.apps import AppConfig


class AlunoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aluno'

    def ready(self):
        import aluno.post_save
        import aluno.templatetags.custom_filters