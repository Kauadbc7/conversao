# Sistema de Conversão de Temperatura
def celsius_para_kelvin(celsius):
    try:
        kelvin = celsius + 273.15
        return kelvin
    except TypeError:
        print("Por favor, insira um número válido para a temperatura em Celsius.")

def kelvin_para_celsius(kelvin):
    try:
        celsius = kelvin - 273.15
        return celsius
    except TypeError:
        print("Por favor, insira um número válido para a temperatura em Kelvin.")

# Condiçao
try:
    celsius = float(input("Digite uma temperatura em celsius °C: "))
    kelvin = celsius_para_kelvin(celsius)
    print(f"{celsius:.2f}°C é igual a {kelvin:.2f}K")
except ValueError:
    print("Por favor, insira um número válido.")

try:
    kelvin = float(input("Digite a temperatura em Kelvin °K : "))
    celsius = kelvin_para_celsius(kelvin)
    print(f"{kelvin:.2f}K é igual a {celsius:.2f}°C")
except ValueError:
    print("Por favor, insira um número válido.")