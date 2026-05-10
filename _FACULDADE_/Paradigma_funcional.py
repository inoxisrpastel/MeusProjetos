from functools import reduce

# Lista de valores simulando um volume de dados
valores = [10, 30, 35, 55, 65]

# Função pura que dobra um valor
def triplicar(x):
    return x * 3

# Pipeline funcional:
# 1) triplica valores
# 2) Filtra os maiores que 100
# 3) Soma todos
resultado = reduce(
    lambda a, b: a + b,
    filter(lambda x: x > 100, map(triplicar, valores))
)

print(resultado)
