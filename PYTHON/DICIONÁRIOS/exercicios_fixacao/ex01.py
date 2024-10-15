# A partir do dicionário abaixo, adicione um novo livro e atualize o ano
# de prublicação de um livro existente. Exiba o dicionário atualizado.

biblioteca = {
    "1984": {"autor": "George Orwell", "ano": 1949},
    "O Senhor dos Anéis": {"autor": "J.R.R. Tolkien", "ano": 1954},
    "O Hobbit": {"autor": "J.R.R. Tolkien", "ano": 1937}
}

print(f"ANTES de atualizado {biblioteca}")

# adicionando novo livro
biblioteca = {
    "O Príncipe": {"autor": "Nicolau Maquiavel", "ano": 1532}
}

# atualizando ano de publicacao
biblioteca["1984"] = 2024

# Depois de atualizado
print(f"DEPOIS de atualizado {biblioteca}")
