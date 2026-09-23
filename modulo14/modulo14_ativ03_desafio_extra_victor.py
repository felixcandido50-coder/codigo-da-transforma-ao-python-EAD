'''




'''

# ==========================================
# 1. VIEW COM BUSCA E PAGINAÇÃO (views.py)
# ==========================================
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Produto

def produto_list(request):
    # Obtém o termo de busca enviado pela URL (ex: ?busca=teclado)
    busca = request.GET.get('busca', '')
    
    # Se houver busca, filtra por nome (icontains ignora maiúsculas/minúsculas)
    if busca:
        produtos_list = Produto.objects.filter(nome__icontains=busca)
    else:
        produtos_list = Produto.objects.all()

    # Configura a paginação para exibir 5 produtos por página
    paginator = Paginator(produtos_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'produtos/produto_list.html', {
        'page_obj': page_obj,
        'busca': busca
    })


# ==========================================
# 2. ROTAS (urls.py)
# ==========================================
from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
]


# ==========================================
# 3. TEMPLATE COM BUSCA E NAVEGAÇÃO DE PÁGINAS (produto_list.html)
# ==========================================
"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Produtos - Com Busca e Paginação</title>
</head>
<body>
    <h1>Produtos Cadastrados</h1>
    <a href="{% url 'produto_create' %}">Cadastrar Novo Produto</a>
    <hr>

    <!-- Formulário de Pesquisa por Nome -->
    <form method="GET" action="">
        <input type="text" name="busca" placeholder="Buscar por nome..." value="{{ busca }}">
        <button type="submit">Pesquisar</button>
        {% if busca %}
            <a href="{% url 'produto_list' %}">Limpar busca</a>
        {% endif %}
    </form>
    <br>

    <!-- Tabela de Produtos Exibindo a Página Atual -->
    <table border="1" cellpadding="8">
        <thead>
            <tr>
                <th>Nome</th>
                <th>Descrição</th>
                <th>Preço</th>
                <th>Quantidade</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            {% for produto in page_obj %}
            <tr>
                <td>{{ produto.nome }}</td>
                <td>{{ produto.descricao }}</td>
                <td>R$ {{ produto.preco }}</td>
                <td>{{ produto.quantidade }}</td>
                <td>
                    <a href="{% url 'produto_update' produto.pk %}">Editar</a> | 
                    <a href="{% url 'produto_delete' produto.pk %}">Excluir</a>
                </td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="5">Nenhum produto encontrado.</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <!-- Controles da Paginação (Anterior / Próxima) -->
    <br>
    <div>
        {% if page_obj.has_previous %}
            <a href="?page=1{% if busca %}&busca={{ busca }}{% endif %}">&laquo; Primeira</a>
            <a href="?page={{ page_obj.previous_page_number }}{% if busca %}&busca={{ busca }}{% endif %}">Anterior</a>
        {% endif %}

        <span>Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}</span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}{% if busca %}&busca={{ busca }}{% endif %}">Próxima</a>
            <a href="?page={{ page_obj.paginator.num_pages }}{% if busca %}&busca={{ busca }}{% endif %}">Última &raquo;</a>
        {% endif %}
    </div>
</body>
</html>
"""