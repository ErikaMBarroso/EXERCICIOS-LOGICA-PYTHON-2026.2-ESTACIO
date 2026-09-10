# Análise de temperaturas registradas em uma semana

temperaturas = []

for i in range (1,8):
    temp = float(input(f"Digite a temperatura no {i}° dia da semana: "))
    temperaturas.append(temp)

maior = temperaturas[0]
menor = temperaturas[0]

for i in temperaturas:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

soma = 0

for t in temperaturas:
    soma = soma + t

media = soma / len(temperaturas)

diasAcimaDaMedia = []

for t in temperaturas:
    if t > media:
        diasAcimaDaMedia.append(t)

temperaturasFormatadas = " ".join([f"{t}°" for t in temperaturas])

print(f"{temperaturasFormatadas}")
print(f"Maior temperatura: {maior}°")
print(f"Menor temperatura: {menor}°")
print(f"Média: {media:.2f}")
print(f"Quantidade de dias em que a temperatura ficou acima da média: {len(diasAcimaDaMedia)}")