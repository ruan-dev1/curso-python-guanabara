from datetime import date

sx = str(input("Digite o seu sexo biológico:(Masculino ou Feminino) ")).strip().upper()
data = int(input("Digite o ano que você nasceu: "))
ano_atual = date.today().year

# 1. Calcule a idade da pessoa e o ano em que ela faz 18 anos
idade = ano_atual - data
ano_alistamento = data + 18

# 2. Agora compare o ano atual com o ano do alistamento
if ano_atual > ano_alistamento and sx == "MASCULINO":
    passou = ano_atual - ano_alistamento
    print(f"\033[32mVocê nasceu em {data}, tem {idade} anos. Você devia se alistar em {ano_alistamento}, ou seja, há {passou} anos!\033[0m")

elif ano_atual < ano_alistamento and sx == "MASCULINO":
    falta = ano_alistamento - ano_atual
    print(f"\033[31mVocê ainda não tem idade para se alistar. Seu alistamento será em {ano_alistamento}, ainda faltam {falta} anos!\033[0m")

elif ano_atual == ano_alistamento and sx == "MASCULINO":
    print(f"\033[33mVocê tem {idade} anos! {ano_atual} é o ano do seu alistamento obrigatório. Aliste-se já!\033[0m")
else:
    print(f"\033[34mVocê nasceu em {data}, tem {idade} anos. O alistamento militar é obrigatório apenas para pessoas do sexo masculino.\033[0m")
