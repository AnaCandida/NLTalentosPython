#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média. 


print('\nDigite as 4 notas do bimestre: \n')

n1 = float(input('Digite a 1º nota:'))
n2 = float(input('Digite a 2º nota:'))
n3 = float(input('Digite a 3º nota:'))
n4 = float(input('Digite a 4º nota:'))
media = (n1+n2+n3+n4)/4
print('\nA media é ', round(media, 2),'.A notas inseridas foram:', n1,n2,n3,n4, ) 