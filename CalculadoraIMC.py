peso = float(input("Digite seu peso em kg:"))
altura = float(input("Digite sua altura em metros:"))

imc = peso / (altura ** 2)

#classificação

if imc < 18.5:
    categoria = "Magreza"
elif imc < 25:   #ja sabemos que é >= 18.5 aqui
    categoria = "Normal"
elif imc < 30:   #ja sabemos que é >= 30 aqui
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade" 

print(f"imc = {imc:.2f} - {categoria}")               