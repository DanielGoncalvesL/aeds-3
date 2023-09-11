def calcular_ano_bissexto(ano):
  if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    return True
  return False

ano = int(input("Informe o ano: "))

if(calcular_ano_bissexto(ano)):
  print("E bissexto")
else:
  print("Nao e bissexto")
