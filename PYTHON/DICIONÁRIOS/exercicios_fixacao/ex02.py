# A partir do dicionário abaixo, adicione o curso de biologia para Ana e
# remova o curso de quimica da Maria. Exiba o dicionário atualizado.
estudantes = {
    "Ana": ["Matemática", "História"],
    "Pedro": ["Biologia", "Física"],
    "Maria": ["Química", "Matemática"]
}

# adicionando curso de biologia para Ana
estudantes["Ana"].insert(2, "Biologia")

# Removendo curso de quimica
del estudantes["Maria"][0]

print(estudantes)
