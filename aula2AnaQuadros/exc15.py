# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja
# invertida.
# o FULANO
# o FULAN
# o FULA
# o FUL
# o FU
# o F

nome = str(input('Digite o seu nome: ')).upper()
for letra in range(0, len(nome)+1):
 print(nome[letra:])