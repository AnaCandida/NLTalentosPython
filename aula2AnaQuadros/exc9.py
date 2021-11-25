#9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos dos elementos do vetor.



import array as arr

vetor = arr.array('i', [])
contador = 0
soma = 0

while contador <=9:
  num = int(input('Digite um número: '))
  soma+=num
  vetor.append(num)
  contador += 1


print(" A soma dos numeros é:", soma)


