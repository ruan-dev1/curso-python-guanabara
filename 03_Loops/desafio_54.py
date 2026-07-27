from datetime import date 
ano_atual = date.today().year
for pess in range (1,8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {pess}ª pessoa: "))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        print(f"\033[32mA {pess}ª pessoa é maior de idade pois tem {idade} anos!\033[0m")
    else:
        print(f"\033[31mA {pess}ª pessoa é menor de idade pois tem {idade} anos!\033[0m")
