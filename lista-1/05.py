def calcular_ano_bissexto(ano):
  if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    return True
  return False


def calcular_mes_menor_igual_sete(mes, ano):
  if mes == 2 and calcular_ano_bissexto(ano):
    return "29 dias"
  elif mes == 2:
    return "28 dias"
  else:
    if mes % 2 != 0:  
      return "31 dias"
    else:
      return "30 dias"

def calcular_mes_maior_sete(mes):
  if mes % 2 == 0:
    return "31 dias"
  else:
    return "30 dias"


def calcular_dias_mes(mes, ano):
  if mes <= 7:
    return calcular_mes_menor_igual_sete(mes, ano)
  else:
    return calcular_mes_maior_sete(mes)

mes = int(input("Informe o mes: "))

while mes < 1 or mes > 12:
  mes = int(input("Informe o mês novamente"))

ano = int(input("Informe o ano: "))

while ano < 0:
  ano = int(input("Informe o ano novamente: "))

print(calcular_dias_mes(mes,ano))
