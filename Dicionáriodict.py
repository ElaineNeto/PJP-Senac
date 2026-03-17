# Criando um dicionário
aluna = {"id":1, "nome": "Elaine", "nota": 8.5}
pessoa = {"nome": "Cristina", "idade": 34}

# Acessando valores por chave
print("Nome da pessoa:", pessoa["nome"])

#Adicionar e alterar chaves/valores
pessoa["cidade"] = "Palhoça"   # adiciona nova chave
pessoa["idade"] = 35           # altera valor da chave existente
print("Pessoa atualizada:", pessoa)

# Remover chave
removido = pessoa.pop("idade")
print("Valor removido (idade):", removido)
print("Após pop('idade'):", pessoa)

# Tamanho
print("Quantidade de chaves em 'aluna':", len(aluna))

# Listar chaves, valores e itens(pares)
print("chaves de 'aluna':", list(aluna.keys()))
print("Valores de 'aluna':", list(aluna.values()))
print("Itens de 'aluna':", list(aluna.items()))

#verificar se uma chave existe
print("chave 'nota' existe?", "nota" in aluna)

#obter valor com padrão (evita erro se chave não existir)
print("turma (com default):", aluna.get("turma", "não cadastrada"))

# Atualizar várias chaves de uma vez
aluna.update({"nota": 8.5, "turma": "A"})
print("Aluna após updatre:", aluna)

# Iterar sobre dict
for chave, valor in aluna.items():
    print(f"{chave} -> {valor}")