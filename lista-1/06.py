def calcular_ano_bissexto(ano):
  if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    return True
  return False

def calcular_mes_menor_igual_sete(mes, ano):
  if mes == 2 and calcular_ano_bissexto(ano):
    return 29
  elif mes == 2:
    return 28
  else:
    if mes % 2 != 0:  
      return 31
    else:
      return 30

def calcular_mes_maior_sete(mes):
  if mes % 2 == 0:
    return 31
  else:
    return 30


def calcular_dias_mes(mes, ano):
  if mes <= 7:
    return calcular_mes_menor_igual_sete(mes, ano)
  else:
    return calcular_mes_maior_sete(mes)

for ano in range(1901,2000):
  for mes in range(1,12):
    for dia in range(1,calcular_dias_mes(mes,ano)):
      if dia * mes == ano % 100:
        print(f"O dia {dia}/{mes}/{ano} é uma data mágica!")