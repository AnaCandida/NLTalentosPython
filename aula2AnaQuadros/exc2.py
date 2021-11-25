#2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

import array as arr

vetor = arr.array('f', [])
contador = 0

while contador <=9:
  num = float(input('Digite um número: '))
  vetor.append(num)
  contador += 1

vetor.reverse()

print("\n O vetor na ordem inversa é:")
for num in  range(10):
  print(vetor[num])

