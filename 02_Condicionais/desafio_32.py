from datetime import date
ano = int(input("Digite um ano e irei falar se ele é bissexto ou não (digite 0 para o ano atual): "))
if ano == 0:
    ano = date.today().year #pega o ano atual
if (ano %4 == 0 and ano %100 != 0 or ano %400 == 0): #se o resto do 4 for igual a 0 e o resto do 100 for diferente de 0 ou o resto do 400 for igual a 0, então é bissexto (diferente = != e igual =[...]
    print(f"\033[32mO ano {ano} é bissexto\033[0m")
else:
    print(f"\033[31mO ano {ano} não é bissexto\033[0m")
