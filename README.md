
# Verificador de Dependência Linear com Sistema Homogêneo

Este projeto em Python verifica se uma matriz é Linearmente Independente (LI) ou Linearmente Dependente (LD), utilizando a resolução de um sistema linear homogêneo `Ax = 0` e a eliminação de Gauss para mostrar a resolução passo a passo.

## Funcionalidades

- Entrada manual do tamanho e dos valores da matriz.
- Montagem do sistema `Ax = 0` com vetor nulo.
- Exibição da matriz aumentada `A | 0`.
- Aplicação do método de escalonamento de Gauss (eliminação).
- Cálculo do posto (rank) da matriz.
- Verificação automática se a matriz é LI ou LD.
- Mensagens explicativas durante todo o processo.

## Conceitos Envolvidos

- Álgebra Linear
- Sistemas Lineares Homogêneos
- Dependência e Independência Linear
- Posto de uma Matriz
- Eliminação de Gauss

## Como Executar

1. Clone o repositório (se estiver no GitHub):

```
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Execute o script em Python:

```
python li_ld_sistema.py
```

3. Digite os valores da matriz conforme solicitado.

Requisitos:
- Python 3.x
- Biblioteca NumPy (`pip install numpy`)

## Exemplo de Uso

```
Digite o tamanho da sua matriz:
Linhas: 3
Colunas: 2
Digite o valor da posição [0,0]: 1
Digite o valor da posição [0,1]: 2
...
Matriz aumentada A | 0:
[1.00, 2.00, 0.00]
...
Posto: 2
Número de variáveis: 2
⇒ A matriz é LI (Linearmente Independente)
```


