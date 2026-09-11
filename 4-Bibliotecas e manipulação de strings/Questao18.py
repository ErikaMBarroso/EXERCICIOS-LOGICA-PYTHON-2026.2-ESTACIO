# Simulação de lançamento de dados com análise estatística

import random
print("=================PARTE 1=================")
dado1 = random.randint(1, 6)
print(f"Resultado do primeiro dado: {dado1}")

dado2 = random.randint(1, 6)
print(f"Resultado do Segundo dado: {dado2}")

soma = dado1 + dado2
print(f"Soma: {soma}")

print("=========================================")
print("=================PARTE 2=================")

dado1 = []
dado2 = []
for i in range(10):
    resultado1 = random.randint(1, 6)
    dado1.append(resultado1)
    resultado2 = random.randint(1, 6)
    dado2.append(resultado2)

soma = [a + b for a, b in zip(dado1, dado2)]
soma7 = []

for i in soma:
    if i == 7:
        soma7.append(i)

print(dado1)
print(dado2)
if len(soma7) == 1:
    print(f"A soma dos dados foi igual a 7 1 vez")
elif len(soma7) > 1:
    print(f"A soma dos dados foi igual a 7 {len(soma7)} vezes")
else:
    print("A soma dos dados não foi igual a sete em nenhuma das vezes")
