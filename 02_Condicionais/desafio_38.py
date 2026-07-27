numero = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite outro número inteiro: "))
print(f"Você digitou o número {numero} e o número {numero_2}")
if numero > numero_2:
    print(f"O número {numero} é maior que o número {numero_2}")
elif numero < numero_2:
    print(f"O número {numero_2} é menor que o número {numero}")
else:
    print(f"Os números {numero} e {numero_2} são iguais")
