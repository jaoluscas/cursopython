import copy

# Lista de produtos
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumentar os preços dos produtos em 10%
for produto in produtos:
    produto['preco'] *= 1.10

# Gerar uma cópia profunda dos produtos
novos_produtos = copy.deepcopy(produtos)

# Ordenar os produtos por nome decrescente
produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda x: x['nome'], reverse=True)

# Ordenar os produtos por preço crescente
produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda x: x['preco'])

# Exibir os resultados
print("Novos produtos com preços aumentados em 10%:")
for produto in novos_produtos:
    print(produto)

print("\nProdutos ordenados por nome decrescente:")
for produto in produtos_ordenados_por_nome:
    print(produto)

print("\nProdutos ordenados por preço crescente:")
for produto in produtos_ordenados_por_preco:
    print(produto)

