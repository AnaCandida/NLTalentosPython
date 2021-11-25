#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor ímpar. Imprima os três vetores.


import array as arr

vetor = arr.array('i', [])
vPar = arr.array('i', [])
vImpar = arr.array('i', [])
contador = 0

while contador <=19:
  num = int(input('Digite um número: '))
  vetor.append(num)
  if num%2==0:
     vPar.append(num)
  else:
    vImpar.append(num)
  contador += 1


# print("\n O primeiro vetor formado foi:")

print('vetor',vetor)
print('par', vPar)
print('impar',vImpar)

