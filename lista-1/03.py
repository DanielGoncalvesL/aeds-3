import random

maior_numero = 0
cont_max = 0

for i in range(100):
  numero_aleatorio = random.randint(1,100)
  if numero_aleatorio > maior_numero:
    maior_numero = numero_aleatorio
    cont_max = cont_max + 1
    print(f"{numero_aleatorio} (atualizado)")
  else:
    print(numero_aleatorio)

print(f"O maior numero encontrado foi {maior_numero}")
print(f"O número máximo de vezes que o maior valor foi atualizado foi {cont_max} vezes")