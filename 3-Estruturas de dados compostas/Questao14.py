# Sistema de gerenciamento de notas de turma

def validaNota(ordem, nome_aluno):
    while True:
        nota = float(input(f"Digite a {ordem} nota de {nome_aluno}: "))
        if 0 <= nota <= 10:
            return nota
        print("Nota inválida! A nota deve ser entre 0 e 10.")

def calculaMedias(alunos):
    maiorMedia = alunos[0]["media"]
    menorMedia = alunos[0]["media"]

    alunoMaiorMedia = alunos[0]["nome"]
    alunoMenorMedia = alunos[0]["nome"]

    for aluno in alunos:
        if aluno["media"] > maiorMedia:
            maiorMedia = aluno["media"]
            alunoMaiorMedia = aluno["nome"]

        if aluno["media"] < menorMedia:
            menorMedia = aluno["media"]
            alunoMenorMedia = aluno["nome"]

    print("====MELHOR E PIOR MÉDIA====")
    print(f"Aluno com maior média: {alunoMaiorMedia}")
    print(f"Aluno com menor média: {alunoMenorMedia}")
    print("___________________________")


def calculaSituacao(alunos):
    aprovados = []
    recuperacao = []
    reprovados = []

    for a in alunos:
        if a["media"] >= 7:
            aprovados.append(a)

        elif a["media"] >= 5:
            recuperacao.append(a)

        else:
            reprovados.append(a)

    print("===SITUAÇÃO DE APROVAÇÃO===")
    print(f"Aprovados: {len(aprovados)}")
    print(f"De recuperação: {len(recuperacao)}")
    print(f"Reprovados: {len(reprovados)}")
    print("___________________________")


alunos = []

for a in range(1, 6):
    nome = input(f"Digite o nome do {a}° aluno: ")
    nota1 = validaNota("primeira", nome)
    nota2 = validaNota("segunda", nome)
    nota3 = validaNota("terceira", nome)

    media = (nota1 + nota2 + nota3) / 3

    novoAluno = {
        'nome': nome,
        'notas': {
            'nota1': nota1,
            'nota2': nota2,
            'nota3': nota3
        },
        'media': media
    }

    alunos.append(novoAluno)

print("===========ALUNOS===========")

for aluno in alunos:
    print(f"Aluno: {aluno['nome']}")
    print(f"Média: {aluno['media']:.2f}")
    print("___________________________")

calculaMedias(alunos)
calculaSituacao(alunos)
