import random

pretos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]

vermelhos = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

verde = [0,00]

arrays_concatenados = sorted(pretos + vermelhos + verde)

indice = random.randint(0,len(arrays_concatenados) - 1)

numero_sorteado = arrays_concatenados[indice]

if indice == 0:
  print("Pagar 0")
elif indice == 1:
  print("Pagar 00")
else:
  print(f"O resultado da rodada é {numero_sorteado}\nPagar {numero_sorteado}")

  if numero_sorteado in pretos:
    print("Pagar preto")

  if numero_sorteado in vermelhos:
    print("Pagar vermelho")

  if numero_sorteado % 2 == 0:
    print("Pagar par")
  else:
    print("Pagar impar")

  if numero_sorteado <= 18:
    print("Pagar de 1 a 18")
  else:
    print("Pagar de 19 a 36")