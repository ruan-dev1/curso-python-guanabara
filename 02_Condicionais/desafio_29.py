vel = int(input("\033[90mPARE, qual a velocidade de seu carro? "))
soma = (vel - 80)*7
if vel > 80:
    print("\033[31mMULTADO!, você excedeu o limite permitido que é de 80km/h\033[0m")
    print("\033[90mVocê deve pagar uma multa por ultrapassar o limite de velocidade permitido, o valor da multa é de R$7,00 por cada km acima do limite permitido.\033[0m")
    print(f"\033[31mO valor da sua multa é de  R$ {soma:.2f}\033[0m")
else:
    print("\033[32mOk, tenha um bom dia! Dirija com segurança!\033[0m")
