from django.urls import path
from core import settings
from erp.views import DashboardView, ErpLoginView, ErpLogoutView, HomeView, ProdutoCreateView, ProdutoDeleteView
from erp.views import ProdutoDetailView, ProdutoListView, ProdutoUpdateView
from erp.views import VendaCreateView, VendaDeleteView, VendaDetailView, VendaListView
from erp.views import VendaUpdateView, atualiza_funcionario, busca_funcionario_por_id
from erp.views import cria_funcionario, lista_funcionarios


app_name = 'erp'
urlpatterns = [
    path('', HomeView.as_view()),

    # Login
    path('login/', ErpLoginView.as_view(), name='login'),
    path('logout/', ErpLogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Funcionarios
    path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/novo/', cria_funcionario, name='cria_funcionario'),
    path('funcionarios/detalhe/<int:pk>/', busca_funcionario_por_id, name='busca_funcionario_por_id'),
    path('funcionarios/atualiza/<int:pk>/', atualiza_funcionario, name='atualiza_funcionario'),

    # Produtos
    path('produtos/', ProdutoListView.as_view(), name='lista_produtos'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='cria_produto'),
    path('produtos/atualiza/<int:pk>/', ProdutoUpdateView.as_view(), name='atualiza_produto'),
    path('produtos/detalhe/<int:pk>/', ProdutoDetailView.as_view(), name='detalhe_produto'),
    path('produtos/deleta/<int:pk>/', ProdutoDeleteView.as_view(), name='deleta_produto'),

    # Vendas
    path('vendas/', VendaListView.as_view(), name='lista_vendas'),
    path('vendas/novo', VendaCreateView.as_view(), name='cria_venda'),
    path('vendas/atualiza/<int:pk>/', VendaUpdateView.as_view(), name='atualiza_venda'),
    path('vendas/detalhe/<int:pk>/', VendaDetailView.as_view(), name='detalhe_venda'),
    path('vendas/deleta/<int:pk>/', VendaDeleteView.as_view(), name='deleta_venda'),

]

if settings.DEBUG:
    from django.conf.urls.static import static

    # Serve static and media files from development server
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
