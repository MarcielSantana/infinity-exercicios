# buscar telefone de um contato especifico

contatos = {
    "Ana": "1234-5678",
    "Pedro": "8765-4321",
    "Maria": "1357-2468"
}

nome_contato = input('Quem você quer encontrar? ').lower

number_telefone = contatos.get(nome_contato, 'Esse contato não existe aqui')
print(f'Telefone de {nome_contato}: {number_telefone}')
