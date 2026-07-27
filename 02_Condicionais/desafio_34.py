salario = float(input("Qual é o seu salario? "))
conta_1 = salario*1.10
conta_2 = salario*1.15
if salario > 1250:
    print(f"\033[32mVocê recebeu um aumento de 10%! Agora seu salario é no total {conta_1:.2f}\033[0m")
else:
    print (f"\033[32mVocê recebeu um aumento de 15%! Agora seu salario é no total {conta_2:.2f}\033[0m")
