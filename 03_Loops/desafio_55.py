maior = 0
menor = 0

for c in range(1, 6): # Vai rodar 5 vezes
    peso = float(input(f"Peso da {c}ª pessoa: "))
    
    # 🌟 SE FOR A PRIMEIRA PESSOA:
    if c == 1:
        maior = peso
        menor = peso
        
    # 🌟 SE NÃO FOR A PRIMEIRA (rodadas 2, 3, 4 e 5):
    else:
        # Aqui você faz os testes normais:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi de {maior}kg")
print(f"O menor peso lido foi de {menor}kg")
