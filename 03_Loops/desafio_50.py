"""Programa: soma dos números pares entre seis entradas do usuário."""
soma = 0
print("\033[1;34mVocê vai digitar 6 numeros e no final vou apenas fazer a soma dos pares! \033[0m")
for c in range(1, 7):
    num = int(input("\033[1;32mDigite um numero \033[0m"))
    if num % 2 == 0:
        soma += num
print(f"De acordo com meus cálculos 🤓☝️ a soma dos pares é \033[1;32m{soma}\033[0m")
