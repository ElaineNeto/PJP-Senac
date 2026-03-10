# Objetivo: calcular IMC e classificar de forma simples

nome = input("Nome: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)     # aritmeticos
print(f"IMC de {nome}: {imc:.2f}")

# comparação + logicos (faixa simplificada)
baixo_peso = imc < 18.5
normal = (imc >= 18.5) and (imc <25)
sobrepeso = (imc >= 25) and (imc < 30)
obesidade = imc >= 30

print("Baixo peso?", baixo_peso)
print("Normal?", normal)
print("Sobrepes?", sobrepeso)
print("Obesidade?", obesidade)