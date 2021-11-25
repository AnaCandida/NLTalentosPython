# 3 Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


import array as arr

notas = arr.array('f', [])
contador = 0
soma = 0

while contador <=3:
  nota = float(input('\nDigite a nota: '))
  notas.append(nota)
  soma += nota
  contador += 1

media = soma/4
print('\nA media é ', round(media, 2),'.As notas inseridas foram:' )
for nota in  range(4):
  print(notas[nota]) 


