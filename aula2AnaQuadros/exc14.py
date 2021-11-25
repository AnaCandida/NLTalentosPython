#4. Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em
# formato de escada.
# o F
# o FU
# o FUL
# o FULA
# o FULAN
# o FULANO


nome = str(input('Digite o seu nome: ')).upper()
for letra in range(0, len(nome)+1):
 print(nome[:letra])