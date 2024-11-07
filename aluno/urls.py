from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.aluno, name='aluno'),
    path('administrador/', views.administrador, name='administrador'),
    path('alunos/', views.lista_alunos, name='aluno_alunos'),
    path('alunos-novo', views.aluno_novo, name='aluno_aluno_novo'),
    path('alunos-update/<int:id>', views.aluno_update, name='aluno_aluno_update'),
    path('alunos-delete/<int:id>', views.aluno_delete, name='aluno_aluno_delete'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('minhaconta/', views.minhaconta, name='minhaconta'),

    path('curso/', views.lista_cursos, name='lista_cursos'),
    path('cursonovo/', views.curso_novo, name='curso_novo'),
    path('curso-update/<int:id>', views.curso_update, name='curso_update'),
    path('curso-delete/<int:id>', views.curso_delete, name='curso_delete'),
    path('curso/<int:id>', views.curso_detalhe, name='curso_detalhe'),
    path('curso/changestatus/<int:id>/<int:categoria_licao>/', views.changeStatus, name='change_status'),
    path('curso/<int:curso_id>/licao/novo/', views.licao_novo, name='licao_novo'),

    path('inscricao/', views.lista_inscricoes, name='lista_inscricoes'),
    path('inscricaolista/', views.lista_inscricao, name='lista_inscricao'),
    path('inscricaonovo/', views.inscricao_novo, name='inscricao_novo'),
    path('inscricao-update/<int:id>', views.inscricao_update, name='inscricao_update'),
    path('inscricao-delete/<int:id>', views.inscricao_delete, name='inscricao_delete'),

    path('licao/<int:id>/', views.lista_Licao, name='lista_licao'),
    path('licao-lista/<int:id>', views.licao_detalhe, name='licao_detalhe'),
    path('licao-update/<int:id>', views.licao_update, name='licao_update'),
    path('licao-delete/<int:id>', views.licao_delete, name='licao_delete'),
    path('download/<int:licao_id>/', views.download_licao, name='download_licao'),

    path('digitacao/', views.lista_digitacao, name='lista_digitacao'),
    path('digitacao-novo/', views.digitacao_novo, name='digitacao_novo'),
    path('digitacao-update/<int:id>', views.digitacao_update, name='digitacao_update'),
    path('digitacao-delete/<int:id>', views.digitacao_delete, name='digitacao_delete'),

    path('inscricao-digitacao/', views.lista_inscricaodigitacao, name='lista_inscricaodigitacao'),
    path('inscricao-digitacao-novo/', views.inscricaodigitacao_novo, name='inscricaodigitacao_novo'),
    path('inscricao-digitacao-update/<int:id>', views.inscricaodigitacao_update, name='inscricaodigitacao_update'),
    path('inscricao-digitacao-delete/<int:id>', views.inscricaodigitacao_delete, name='inscricaodigitacao_delete'),

    path('cursodigitacao/<int:id>', views.cursodigitacao_detalhe, name='cursodigitacao_detalhe'),
    path('cursodigitacao/next/<int:id>', views.cursodigitacao_next, name='cursodigitacao_next'),
    path('cursodigitacao/relatorioDigitacao/', views.relatorioDigitacao, name='relatorioDigitacao'),
    path('cursodigitacao/relatorioDigitacao/relatorio', views.obter_relatorioDigitacao, name='obter_relatorioDigitacao'),
    path('rankindigitacao/', views.rankindigitacao, name='rankindigitacao'),

    path('provasdigitacao/<int:id>', views.provasdigitacao, name='provasdigitacao'),
    path('provasdigitacao/prova/', views.criar_prova_digitacao, name='criar_prova_digitacao'),  
    path('prova/<int:curso_id>/', views.prova, name='prova'),
    path('processar-respostas/<int:curso_id>/', views.processar_respostas, name='processar_respostas'),
    path('resultado-prova/<int:curso_id>/', views.resultado_prova, name='resultado_prova'),
    path('prova/questoes/<int:id>', views.questoes_detalhe, name='questoes_detalhe'),

    path('itens_detalhe/<int:curso_id>/<int:questao_id>', views.itens_detalhe, name='itens_detalhe'),
    path('item/delete/<int:item_id>', views.excluir_item, name='excluir_item'),
    path('item/editar/<int:item_id>', views.editar_item, name='editar_item'),
    path('questao/criar/<int:curso_id>/', views.criar_questao, name='criar_questao'),
    path('questao/editar/<int:questao_id>', views.editar_questao, name='editar_questao'),
    path('questao/delete/<int:questao_id>', views.excluir_questao, name='excluir_questao'),
    
    path('curso/certificado/<int:curso_id>/', views.gerar_certificado, name='gerar_certificado'),
    path('curso/certificado/teste/<int:curso_id>/', views.certificadoteste, name='certificadoteste'),
    path('curso/certificado/gerar_pdf/<int:curso_id>/', views.render_pdf_view, name='render_pdf_view'),
    path('curso/certificado/gerar_pdfDig/', views.render_pdf_digitacao_view, name='render_pdf_digitacao_view'),

    path('marcar-tour-completo/', views.marcar_tour_completo, name='marcar_tour_completo'),
    path('toggle-tour-status/', views.toggle_tour_status, name='toggle_tour_status'),
    path('marcar-tour-completodigi/', views.marcar_tour_completoDig, name='marcar_tour_completoDig'),
    path('toggle-tour-status-dig/', views.toggle_tour_status_dig, name='toggle_tour_status_dig'),
]
