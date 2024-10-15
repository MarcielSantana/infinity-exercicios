# perguntar se quer adicionar mais contato e adicionando novos contatos
contatos = {
    "Ana": "1234-5678",
    "Pedro": "8765-4321",
    "Maria": "1357-2468"
}


while True:
    novo_contato = input('''Deseja adicionar mais algum contato? (s/n):
    ''').strip().lower()
# O método strip() em Python remove espaços em branco no início
# e no final de uma cadeia de caracteres
    if novo_contato == 's':
        nome = input('Nome: ').strip()
        telefone = input('Telefone: ').strip()
        contatos[nome] = telefone
    elif novo_contato == 'n':
        break
    else:
        print('Resposta errada. Tente novamente')

print(contatos)
