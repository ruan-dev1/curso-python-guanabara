print('\033[33m-=' * 20)
print('\033[33mANALISADOR DE TRIÂNGULOS\033[0m')
print('\033[33m-=\033[0m' * 20)
lado1 = float(input('Digite o valor do primeiro comprimento: '))
lado2 = float(input('Digite o valor do segundo comprimento: '))
lado3 = float(input('Digite o valor do terceiro comprimento: '))
if lado1 >= lado2 + lado3 or lado2 >= lado3 + lado1 or lado3 >= lado1 + lado2:
    print('\033[31mEsse comprimento que você digitou acima NÃO PODEM FORMAR um triângulo!\033[0m')
elif lado1 == lado2 == lado3:
    print('\033[34mEsse triângulo é do tipo EQUILÁTERO!\033[0m')  
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 or lado3 == lado2:
    print('\033[34mEsse triângulo é do tipo ISÓSCELES!\033[0m')
else:   print('\033[34mEsse triângulo é do tipo ESCALENO!\033[0m')

#OU (jeito do professor, mais organizado e fácil de ler)

#r1 = float(input('Primeiro segmento: '))
#r2 = float(input('Segundo segmento: '))
#r3 = float(input('Terceiro segmento: '))

# SE PODEM FORMAR UM TRIÂNGULO:
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  #  print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    
    # [Bloco Interno] Só roda se a linha de cima for verdadeira
   # if r1 == r2 == r3:
   #     print('EQUILÁTERO!')
   # elif r1 != r2 != r3 != r1:
   #     print('ESCALENO!')
   # else:
   #     print('ISÓSCELES')
