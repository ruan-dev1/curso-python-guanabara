from time import sleep
valores_na_linha = 0  # Controla quantos números já foram pra tela na mesma linha
soma = 0
input("\033[32;1mVou contar de 1 até 500 mais somente os números ímpares que são múltiplos de 3!:\033[0m\nOk? ")
print("\033[32;1mFechou! Vou iniciar!\033[0m")
print("\033[32;1mContando...\033[0m")
sleep(1)
for c in range(1, 500, 2):
    if c % 3 == 0:
        print(f"{c:3}", end=" ")  # O :3 serve para alinhar os números bonitinho
        valores_na_linha += 1     # Contou +1 número na linha atual
        # Se já imprimiu 10 números, quebra a linha!
        soma += c
        if valores_na_linha == 10:
            print()               # Print vazio = Quebra de linha no terminal
            valores_na_linha = 0  # Reseta o contador para a próxima linha
        sleep(0.1)  # Dá uma pausa de 0.1 segundos entre cada número para ficar mais legal


print(f"\n\033[32;1mAgora de extra vou fazer a soma de todos eles que dá: {soma}\033[0m")
