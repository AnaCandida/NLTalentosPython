#8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

import array as arr
idades = arr.array('i', [])
alturas = arr.array('i', [])

contador = 0

while contador <=4:
  idade = int(input('Digite a sua idade: '))
  altura = int(input('Digite a sua altura em cm: '))
  idades.append(idade)
  alturas.append(altura)

  contador += 1

for altura in alturas:
    # altura = {%2}.format(altura)
    altura = str(round(altura, 2))


alturas.reverse()
print(alturas)  

idades.reverse()
print(idades)

