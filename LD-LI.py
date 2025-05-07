
import numpy as np

def exibir_matriz(m):
    for linha in m:
        print(["{:.2f}".format(elem) for elem in linha])

# Ler tamanho da matriz
print("Digite o tamanho da sua matriz:")
x = int(input("Linhas: "))
y = int(input("Colunas: "))

# Se existir mais colunas do que linhas → LD
if y > x:
    print("Mais colunas do que linhas ⇒ Matriz é LD (Linearmente Dependente)")
    exit()

# Ler matriz
matrizP = []
for i in range(x):
    linha = []
    for j in range(y):
        valor = float(input(f"Digite o valor da posição [{i},{j}]: "))
        linha.append(valor)
    matrizP.append(linha)

matrizP = np.array(matrizP)

# Criar vetor nulo (lado direito do sistema Ax = 0)
vetorNulo = np.zeros((x, 1))

# Matriz aumentada A | 0
matriz_estendida = np.hstack((matrizP, vetorNulo))

print("\nSistema homogêneo montado (matriz aumentada A | 0):")
exibir_matriz(matriz_estendida)

# Escalonamento usando eliminação de Gauss (redução para escada)
matriz_escalonada = matriz_estendida.astype(float).copy()
linhas, colunas = matriz_escalonada.shape

# Redução para forma escalonada
for i in range(min(x, y)):
    # Pivô diferente de zero
    if matriz_escalonada[i][i] == 0:
        for k in range(i+1, x):
            if matriz_escalonada[k][i] != 0:
                matriz_escalonada[[i, k]] = matriz_escalonada[[k, i]]
                break

    # Zerando abaixo do pivô
    for k in range(i+1, x):
        if matriz_escalonada[i][i] != 0:
            fator = matriz_escalonada[k][i] / matriz_escalonada[i][i]
            matriz_escalonada[k] = matriz_escalonada[k] - fator * matriz_escalonada[i]

print("\nMatriz após escalonamento (eliminação de Gauss):")
exibir_matriz(matriz_escalonada)

# Calcular posto (número de linhas não nulas)
posto = 0
for linha in matriz_escalonada:
    if not np.allclose(linha[:-1], 0):  # desconsidera a última coluna (vetor nulo)
        posto += 1

print(f"\nPosto da matriz dos coeficientes: {posto}")
print(f"Número de variáveis (colunas): {y}")

# Verificação final
if posto == y:
    print("A matriz é LI (Linearmente Independente) ⇒ única solução trivial x = 0.")
else:
    print("A matriz é LD (Linearmente Dependente) ⇒ sistema com infinitas soluções.")


