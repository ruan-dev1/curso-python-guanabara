s = 1
while s == 1:
    sex = input("\033[33mDigite o sexo da pessoa (M ou F): \033[0m").strip().upper()
    if sex == "M" or sex == "F":
        print("\033[32mSexo registrado com sucesso!\033[0m")
        break
    else:
        print("\033[31mEntrada inválida. Por favor, digite 'M' para masculino ou 'F' para feminino.\033[0m")
