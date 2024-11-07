from django.contrib import admin
from .models import (
    Aluno,
    Curso,
    Inscricao,
    Licao,
    ConclusaoLicao,
    Digitacao,
    InscricaoDigitacao,
    RelatorioDigitacao,
    DigitacaoDetalhes,
    ProvaDigitacao,
    Questao,
    ItemQuestao,
    Resposta,
)

admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Licao)
admin.site.register(Inscricao)
class ConclusaoLicaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'licao', 'curso', 'status', 'data_conclusao')

admin.site.register(ConclusaoLicao, ConclusaoLicaoAdmin)
class DigitacaoAdmin(admin.ModelAdmin):
    list_display = ('ordem', 'descricao', 'repeticao', 'licao', 'fase')
admin.site.register(Digitacao, DigitacaoAdmin)
admin.site.register(InscricaoDigitacao)
admin.site.register(DigitacaoDetalhes)
@admin.register(RelatorioDigitacao)
class RelatorioDigitacaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'licao_atual', 'data_acesso', 'tempo', 'toques', 'acertos', 'erros')
    list_filter = ('aluno', 'data_acesso')
    search_fields = ('aluno__username', 'licao_atual')
admin.site.register(ProvaDigitacao)
admin.site.register(Questao)
admin.site.register(ItemQuestao)
admin.site.register(Resposta)