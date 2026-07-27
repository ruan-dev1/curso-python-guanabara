c = 1
n = int(input("Digite o primero termo "))
r = int(input("Digite a razão da PA: "))
cores = {"amarelo": "\033[1;33m",
          "verde": "\033[1;32m",
            "azul": "\033[1;34m",
              "vermelho": "\033[1;31m", 
              "limpa": "\033[m"}
total_termos = 10
while c <= total_termos:
    if c < total_termos:
        print(f"{cores['amarelo']}{n}{cores['limpa']}", end = " --> ")
    else: 
        print(f"{cores['amarelo']}{n}{cores['limpa']}")
    n += r
    c += 1
    
while True:
    p = str(input("Não acabou! Você gostaria de ver mais termos dessa razão de PA? Digite APENAS sim ou não: ")).upper().strip()
    if p == "SIM" or p == "S":
        termos_a_mais = int(input("Beleza! quantos termos você quer ver a mais? "))
        total_termos += termos_a_mais
        while c <= total_termos:
            if c < total_termos:
                print(f"{cores['amarelo']}{n}{cores['limpa']}", end = " --> ")
            else:
                print(f"{cores['amarelo']}{n}{cores['limpa']}")
            c += 1
            n += r
        
    elif p == "NÃO" or p == "N" or p == "NAO":
        print(f"{cores['verde']}Ok! Paramos por aqui, o total foi de {total_termos} termos. Até mais!{cores['limpa']}")
        break
    elif p != "SIM" and p != "NÃO" and p != "S" and p != "N" and p != "NAO":
        print(f"{cores['vermelho']}Inválido! Por favor, digite apenas sim ou não de maneira corrreta.{cores['limpa']}")
    

    
