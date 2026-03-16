frutas = ["maça", "banana", "kiwi", "pera"]
numeros = [1, 2, 3, 4, 5]

# Acessar elementos
print("Primeira fruta:", frutas[0])  # maça
print("Ultima fruta:", frutas[-1])  # pera

# Modificar elementos
frutas[1] = "banana da terra"
print("Frutas modificadas:", frutas)

# Adicionar elementos
frutas.append("uva")    # adiciona no final
frutas.insert(1, "pera")  # adiciona na posição 1 
print("Frutas após adição:", frutas)

# Remover elementos
frutas.remove("maça")  # remove pelo valor
ultima = frutas.pop()  # remove e retorna o ultimo 
print("Após remover 'maça' e pop():", frutas, "| Ultimo removido:", ultima)
