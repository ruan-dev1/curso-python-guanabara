nome = str(input("Digite seu nome completo: "))
print(f"O seu nome com todas as letras maiúsculas é: {nome.upper()}")
print(f"O seu nome com todas as letras mínusculas é: {nome.lower()}")
print(f"O seu nome tem ao todo {len(nome.replace(' ', '',))} letras") 
sla = nome.split ()
print(f"Seu nome tem ao todo {len(nome)-nome.count (' ')}")
# 1. Para contar as letras menos os espaços
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.")
# 2. Para saber onde termina o primeiro nome (contando a posição do primeiro espaço)
print(f"Seu primeiro nome tem {nome.find(' ')} letras.")
#ou
print(f"O seu nome tem ao todo {len(nome.replace(' ', ''))} letras")
