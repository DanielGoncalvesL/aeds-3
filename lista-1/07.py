limite = int(input("Informe o limite: "))

while limite < 2:
  limite = int(input("Informe o limite novamente: "))

p = 2

lista_primos = list(range(p,limite + 1))

while p < limite:
  for numero in lista_primos:
    if numero % p == 0 and numero != p:
      lista_primos.remove(numero)
  if len(lista_primos) > lista_primos.index(p) + 1:
    p = lista_primos[lista_primos.index(p) + 1]
  else:
    p = limite + 1

print(lista_primos)