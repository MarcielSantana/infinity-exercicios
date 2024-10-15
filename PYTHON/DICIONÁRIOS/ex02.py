# Dado o dicionário 'contato' com as seguintes chaves e valores:

contato = {
    "telefone": "123456789",
    "email": "contato@exemplo.com"
}

print(f"ANTES da atualização {contato}")

# atualizando o valor de uma chave
contato["telefone"] = "987654321"
print(f"DEPOIS da atualização passa a ser {contato}")
