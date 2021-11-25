#4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

import array as arr
import re

consoantes = arr.array('u', [])
contador = 0

for i in range(10):
	caractere = input('\nDigite um caractere: ')
	caractere.upper()
	consoantes.append(caractere)
 

consoantes.remove('a')
consoantes.remove('e')
consoantes.remove('i')
consoantes.remove('o')
consoantes.remove('u')

print('Foram digitadas: ', len(consoantes),'consoantes:', consoantes, )


	



  