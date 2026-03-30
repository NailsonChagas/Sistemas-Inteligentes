from collections import deque

# estado: (Me, Ce, Md, Cd, B)
estado_inicial = (3, 3, 0, 0, 'E')
estado_objetivo = (0, 0, 3, 3, 'D')

# possíveis ações (M, C, nome)
acoes = [
    (1, 0, "1M"),
    (2, 0, "2M"),
    (0, 1, "1C"),
    (0, 2, "2C"),
    (1, 1, "1M1C")
]

def estado_valido(Me, Ce, Md, Cd):
    if not (0 <= Me <= 3 and 0 <= Ce <= 3 and 0 <= Md <= 3 and 0 <= Cd <= 3):
        return False
    
    if (Me > 0 and Me < Ce):
        return False
    if (Md > 0 and Md < Cd):
        return False
    
    return True

def gerar_sucessores(estado):
    Me, Ce, Md, Cd, B = estado
    sucessores = []

    for m, c, nome in acoes:
        if B == 'E':
            novo = (Me - m, Ce - c, Md + m, Cd + c, 'D')
            acao = f"{nome} -> E->D"
        else:
            novo = (Me + m, Ce + c, Md - m, Cd - c, 'E')
            acao = f"{nome} -> D->E"

        if estado_valido(*novo[:4]):
            sucessores.append((novo, acao))

    return sucessores

def bfs():
    fila = deque()
    fila.append((estado_inicial, []))
    visitados = set()

    while fila:
        estado, caminho = fila.popleft()

        if estado in visitados:
            continue

        visitados.add(estado)

        if estado == estado_objetivo:
            return caminho

        for sucessor, acao in gerar_sucessores(estado):
            fila.append((sucessor, caminho + [(estado, acao, sucessor)]))

    return None

# executar
solucao = bfs()

# imprimir resultado
if solucao:
    print("Solução ótima:\n")
    for estado, acao, novo_estado in solucao:
        print(f"{estado} -> {acao} -> {novo_estado}")
else:
    print("Nenhuma solução encontrada.")