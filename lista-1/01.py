# print("Informe a quantidade de paes dormidos comprados:")
def formatar_numero(numero):
  return "{:.2f}".format(numero)

quantidadePaes = int(input("Informe a quantidade de paes dormidos comprados: "))

while quantidadePaes <= 0:
  quantidadePaes = int(input("Informe a quantidade de paes dormidos comprados novamente: "))


valor = quantidadePaes * 4.6

valorFinalDesconto = valor * 0.6

valorDesconto = valor - valorFinalDesconto

print(f"Valor sem desconto: {formatar_numero(valor)}\nDesconto: {formatar_numero(valorDesconto)}\nValor final: {formatar_numero(valorFinalDesconto)}")
