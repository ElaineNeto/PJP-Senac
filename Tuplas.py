#Criando tuplas
coordenadas = (10, 20)
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

# Acessando elementos
print("x:", coordenadas[0], "| Y:", coordenadas[1])

# Slicing(fatiamento) em tuplas
print("Primeiros três dias:", dias[:3])

#Tamanho
print("Tamanho da tupla 'dias':", len(dias))

# Verificar se um elemento esta na tupla
print("tem 'segunda'?", "segunda" in dias)

# Contagem de indice em tuplas
print("contagem de 'terça':", dias.count("terça"))
print("Índice de 'quarta':", dias.index("quarta"))