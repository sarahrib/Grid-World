import random

def fazer_grid(linhas, colunas):
  grid = []
  
  for linha in range(linhas):
    linha = []
    for col in range(colunas):
      linha.append(0)

    grid.append(linha)
  
  return grid

def visualizar_grid(grid):
    for linha in grid:
        print(' '.join(str(celula) for celula in linha))

def acoes_possiveis(grid, posicao):
    linhas, colunas = len(grid), len(grid[0])
    x, y = posicao
    acoes = []

    if x > 0 and grid[x-1][y] >= 0: # para cima
        acoes.append((x-1, y))
    if x < linhas - 1 and grid[x+1][y] >= 0: # para baixo
        acoes.append((x+1, y))
    if y > 0 and grid[x][y-1] >= 0: # esquerda
        acoes.append((x, y-1))
    if y < colunas - 1 and grid[x][y+1] >= 0: # direita
        acoes.append((x, y+1))

    return acoes

def recompensa(grid, posicao):
    if grid[posicao[0]][posicao[1]] == -1: # Montanha
        return -100
    elif grid[posicao[0]][posicao[1]] == -2: # Areia movediça
        return -1000
    else:
        return -1 # Recompensa padrão por movimento

def mover_agente(grid, inicio, fim):
    posicao = inicio
    while True:
        if posicao == fim:
            print("Chegou ao destino!")
            return
        elif grid[posicao[0]][posicao[1]] == -2:
            print("Caiu na areia movediça!")
            return

        acoes = acoes_possiveis(grid, posicao)
        if not acoes: # Sem movimentos possíveis
            print("Sem mais movimentos possíveis.")
            return

        # Escolhe uma ação aleatória (aqui pode ser implementada uma lógica mais sofisticada)
        posicao = random.choice(acoes)
        print(f"Moveu para {posicao}, Recompensa: {recompensa(grid, posicao)}")

# Exemplo de uso
grid = fazer_grid(8, 8)
grid[1][1] = -1 # Montanhas
grid[2][3] = -1 # Montanhas
grid[5][4] = -2 # Areia movediça
grid[5][5] = -2 # Areia movediça

inicio = (0, 0)
fim = (7, 7)

visualizar_grid(grid)
mover_agente(grid, inicio, fim)
