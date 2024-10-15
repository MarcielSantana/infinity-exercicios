# classifique os alunos em "aprovado" (media >= 7) e "Reprovado" (media < 7).
# Exiba duas listas: uma para alunos aprovados e outra para alunos reprovados
notas_alunos = {
    "Ana": [8.5, 9.0, 7.5],
    "Pedro": [5.5, 6.0, 7.0],
    "Maria": [7.0, 7.5, 6.0]
}

aprovados = {}
reprovados = {}

for alunos, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    if media >= 7:
        aprovados[alunos] = (notas, media)
    else:
        reprovados[alunos] = (notas, media)

print('Alunos APROVADOS:')
for alunos, (notas, media) in aprovados.items():
    print(f'{alunos}: Notas: {notas}, Média: {media:.2f}')

print('Alunos REPROVADOS:')
for alunos, (notas, media) in reprovados.items():
    print(f'{alunos}: Notas: {notas}, Média: {media:.2f}')
