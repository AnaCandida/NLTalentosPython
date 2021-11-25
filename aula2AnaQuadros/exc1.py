#1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

import array as arr

vetor = arr.array('i', [])
contador = 0

while contador <=4:
  num = int(input('Digite um número: '))
  vetor.append(num)
  contador += 1

print("\n O vetor formado foi:")

for num in  range(5):
  print(vetor[num])


