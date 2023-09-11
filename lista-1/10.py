def distancia_edicao(s1, s2):
    # Caso base: se uma das strings estiver vazia, o custo é a outra string
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    # Verifica se os últimos caracteres são iguais
    if s1[-1] == s2[-1]:
        custo = 0
    else:
        custo = 1

    # Chamadas recursivas para as três operações possíveis
    deletar = distancia_edicao(s1[:-1], s2) + 1
    inserir = distancia_edicao(s1, s2[:-1]) + 1
    substituir = distancia_edicao(s1[:-1], s2[:-1]) + custo

    # Retorna o mínimo entre as três operações
    return min(deletar, inserir, substituir)

s1 = input("Informe a primeira palavra: ")
s2 = input("Informe a segunda palavra: ")

distancia = distancia_edicao(s1, s2)
print(f"A distância de edição entre '{s1}' e '{s2}' é {distancia}")
