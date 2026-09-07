# Conversão entre escalas termométricas

def celciusParaFahrenheit(tempC):
    tempF = tempC * 9 / 5 + 32
    print(f"{tempC:.2f} °C = {tempF:.2f} °F")

def celciusParaKelvin(tempC):
    tempK = tempC + 273.15
    print(f"{tempC:.2f} °C = {tempK:.2f} K")

tempC = float(input("Digite a temperatura em Celsius:").replace(',','.'))

celciusParaFahrenheit(tempC)
celciusParaKelvin(tempC)