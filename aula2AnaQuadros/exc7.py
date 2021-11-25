#7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import array as arr

numeros = arr.array('i', [])
soma = 0
multiplicacao = 0
contador = 0

while contador <=19:
  num = int(input('Digite um número: '))
  numeros.append(num)
  soma += num
  multiplicacao += num*num
  contador += 1


print('Soma = ', soma)
print('Multiplicação = ', multiplicacao)
print('Numeros = ', numeros)


