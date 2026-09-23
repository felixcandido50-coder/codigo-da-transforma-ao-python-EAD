# ==========================================
# 1. MODELS (models.py)
# ==========================================
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_field_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome


# ==========================================
# 2. VIEWS (views.py)
# ==========================================
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

# Listagem simples dos produtos
def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produto_list.html', {'produtos': produtos})

# Criar produto
def produto_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        
        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            quantidade=quantidade
        )
        return redirect('produto_list')
    return render(request, 'produtos/produto_form.html')

# Atualizar produto
def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')
        produto.save()
        return redirect('produto_list')
    return render(request, 'produtos/produto_form.html', {'produto': produto})

# Deletar produto
def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, 'produtos/produto_confirm_delete.html', {'produto': produto})


# ==========================================
# 3. URLS (urls.py)
# ==========================================
from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('novo/', views.produto_create, name='produto_create'),
    path('editar/<int:pk>/', views.produto_update, name='produto_update'),
    path('deletar/<int:pk>/', views.produto_delete, name='produto_delete'),
]


# ==========================================
# 4. TEMPLATES (HTMLs)
# ==========================================

"""
--- ARQUIVO: templates/produtos/produto_list.html ---
"""
"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Produtos</title>
</head>
<body>
    <h1>Produtos Cadastrados</h1>
    <a href="{% url 'produto_create' %}">Cadastrar Novo Produto</a>
    <hr>

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
            {% for produto in produtos %}
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
                <td colspan="5">Nenhum produto cadastrado.</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

"""
--- ARQUIVO: templates/produtos/produto_form.html ---
"""
"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{% if produto %}Editar{% else %}Novo{% endif %} Produto</title>
</head>
<body>
    <h1>{% if produto %}Editar{% else %}Cadastrar{% endif %} Produto</h1>

    <form method="POST">
        {% csrf_token %}
        <label>Nome:</label><br>
        <input type="text" name="nome" value="{{ produto.nome|default:'' }}" required><br><br>

        <label>Descrição:</label><br>
        <textarea name="descricao" required>{{ produto.descricao|default:'' }}</textarea><br><br>

        <label>Preço:</label><br>
        <input type="number" step="0.01" name="preco" value="{{ produto.preco|default:'' }}" required><br><br>

        <label>Quantidade:</label><br>
        <input type="number" name="quantidade" value="{{ produto.quantidade|default:'' }}" required><br><br>

        <button type="submit">Salvar</button>
        <a href="{% url 'produto_list' %}">Cancelar</a>
    </form>
</body>
</html>
"""

"""
--- ARQUIVO: templates/produtos/produto_confirm_delete.html ---
"""
"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Excluir Produto</title>
</head>
<body>
    <h1>Excluir Produto</h1>
    <p>Tem certeza que deseja excluir o produto <strong>"{{ produto.nome }}"</strong>?</p>

    <form method="POST">
        {% csrf_token %}
        <button type="submit">Confirmar Exclusão</button>
        <a href="{% url 'produto_list' %}">Cancelar</a>
    </form>
</body>
</html>
"""