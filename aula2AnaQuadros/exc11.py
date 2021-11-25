#Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido
# do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e
# são iguais ou diferentes no conteúdo.
# o Compara duas strings
# o String 1: Brasil Hexa 2006
# o String 2: Brasil! Hexa 2006!
# o Tamanho de "Brasil Hexa 2006": 16 caracteres
# o Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# o As duas strings são de tamanhos diferentes.
# o As duas strings possuem conteúdo diferente.


palavraUm = input('Digite a primeira palavra: ')
palavraDois = input('Digite a segunda palavra: ')

print('A lº palavra foi:', palavraUm, '| comprimento:' , len(palavraUm))
print('A 2º palavra foi:', palavraDois, '| comprimento:' , len(palavraDois))

if len(palavraUm)==len(palavraDois):
  print('As duas tem o mesmo tamanho')
else:
  print('Elas tem tamahos diferentes')

if palavraUm == palavraDois:
  print('As duas possuem o mesmo conteúdo')  
else:
  print('As duas possuem conteúdo diferente')