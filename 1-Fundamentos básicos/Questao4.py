# Cálculo de média e determinação de situação acadêmica

nota1 = float(input("Digite a primeira nota:"))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Digite um valor válido:"))

nota2 = float(input("Digite a segunda nota:"))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Digite um valor válido:"))

nota3 = float(input("Digite a terceira nota:"))
while nota3 < 0 or nota3 > 10:
    nota3 = float(input("Digite um valor válido:"))

media = (nota1 + nota2 + nota3) / 3

print(f"{nota1} | {nota2} | {nota3}\nSua média é: {media:.2f}")

if media >= 7:
    print("Você foi aprovado!")
elif media >=5:
    print("Você está de recuperação.") 
else:
    print("Você foi reprovado.")