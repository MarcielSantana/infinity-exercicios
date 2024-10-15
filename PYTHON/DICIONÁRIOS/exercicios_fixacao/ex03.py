# implementar um código para contar o numero total de compras
# feitas por cada cliente

compras_clientes = {
    "Ana": ["leite", "pão", "maçã"],
    "Pedro": ["pão", "arroz", "leite", "maçã"],
    "Maria": ["maçã", "leite"]
}

for cliente, produto in compras_clientes.items():
    print(f"O cliente {cliente} comprou {len(produto)} produtos")
