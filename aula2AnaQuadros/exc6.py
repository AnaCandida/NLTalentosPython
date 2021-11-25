#6. Faça um Programa que imprima a data de hoje e quantos dias faltam para o final do ano.


from datetime import date

dataAtual = date.today()

dataFormatada = '{}/{}/{}' .format(dataAtual.day, dataAtual.month, dataAtual.year)

finalDoAno =  date(dataAtual.year, 12, 31)

dataFinalFormatada = '{}/{}/{}' .format(31, 12, dataAtual.year)

qtsDiasFimAno = abs((finalDoAno - dataAtual).days)

print('A data de hoje é:', dataFormatada,'.Faltam ', qtsDiasFimAno, 'dias para o final do ano.')