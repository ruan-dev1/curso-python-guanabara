num = int(input("Digite um número: "))
contador_divisao = 0
for c in range(1, num + 1):
    if num % c == 0:
        contador_divisao += 1

if contador_divisao == 2:
    print("\033[32mEsse número é primo!\033[0m")
else:
    print("\033[31mEsse número não é um número primo.\033[0m")
