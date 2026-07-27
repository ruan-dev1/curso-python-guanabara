num1 = int(input("\033[0mDigite 1 numero: ")), int(input(
    "\033[0mDigite outro numero: ")), int(input("\033[0mDigite mais um numero: "))
num2 = max(num1)
num3 = min(num1)
if num2 == num3:
    print("\033[34mOs numeros são iguais\033[0m")
else:
    print(f"O numero maior numero é: \033[32m{num2}\033[0m, e o menor numero é: \033[31m{num3}\033[0m.")
