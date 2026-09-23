'''




'''

# ==========================================
# 1. PAINEL DE ADMINISTRAÇÃO (admin.py)
# ==========================================
from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Campos exibidos na tabela principal do admin
    list_display = ('nome', 'preco', 'quantidade')
    
    # Campo de busca no painel de administração
    search_fields = ('nome',)
    
    # Filtros laterais no admin
    list_filter = ('preco',)


# ==========================================
# 2. TESTES AUTOMATIZADOS (tests.py)
# ==========================================
from django.test import TestCase
from django.urls import reverse
from .models import Produto

# Testes para a Model de Produto
class ProdutoModelTest(TestCase):

    def setUp(self):
        # Cria um produto temporário para os testes
        self.produto = Produto.objects.create(
            nome='Teclado Gamer',
            descricao='Teclado mecânico RGB',
            preco=150.00,
            quantidade=10
        )

    def test_criacao_produto(self):
        """Testa se o produto foi salvo corretamente no banco de dados"""
        self.assertEqual(self.produto.nome, 'Teclado Gamer')
        self.assertEqual(self.produto.preco, 150.00)
        self.assertEqual(self.produto.quantidade, 10)
        self.assertEqual(str(self.produto), 'Teclado Gamer')


# Testes para as Views/Rotas de Produto
class ProdutoViewTest(TestCase):

    def setUp(self):
        # Cria um produto temporário para o teste da view
        self.produto = Produto.objects.create(
            nome='Mouse Gamer',
            descricao='Mouse óptico de alta precisão',
            preco=80.00,
            quantidade=5
        )

    def test_view_listagem_produtos(self):
        """Testa se a página de listagem responde com status 200 (OK) e exibe o produto"""
        response = self.client.get(reverse('produto_list'))
        
        # Verifica se a página respondeu com sucesso
        self.assertEqual(response.status_code, 200)
        
        # Verifica se o produto criado está presente no HTML retornado
        self.assertContains(response, 'Mouse Gamer')
        
        # Verifica se o template correto foi utilizado
        self.assertTemplateUsed(response, 'produtos/produto_list.html')