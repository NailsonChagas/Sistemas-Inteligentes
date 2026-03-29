# Você tem três jarros com capacidades de 45 litros, 30 litros e 11 litros, além de uma
# torneira. Pode encher os jarros, esvaziá-los no chão ou transferir água entre eles. É
# necessário medir exatamente 4 litros.

# Um estado é representado pela quantidade de água em cada jarro: (x, y, z), com x sendo o volume de água presente no jarro de 45L, y  sendo o volume de água presente no jarro de 30L e z sendo o volume de água presente no jarro de 11L.
# Ações: 
#     Encher um jarro:
#         (x, y, z) -> (45, y, z)
#         (x, y, z) -> (x, 30, z)
#         (x, y, z) -> (x, y, 11)
#     Esvaziar um jarro:
#         (x, y, z) -> (0, y, z)
#         (x, y, z) -> (x, 0, z)
#         (x, y, z) -> (x, y, 0)
#     Transferir água entre jarros:
#         Exemplo: de x para y, quantidade transferida de água = t = min(x, 30 - y), com o estado resultante da ação sendo (x - t, y + t, z) 

from collections import deque

# capacidades: x=45L, y=30L, z=11L
CAP = (45, 30, 11)
NAMES = ['x', 'y', 'z']


def get_neighbors(state):
    x, y, z = state
    jars = [x, y, z]
    neighbors = []

    # Encher
    for i in range(3):
        new = list(jars)
        new[i] = CAP[i]
        neighbors.append((tuple(new), f"encher {NAMES[i]}"))

    # Esvaziar
    for i in range(3):
        new = list(jars)
        new[i] = 0
        neighbors.append((tuple(new), f"esvaziar {NAMES[i]}"))

    # Transferir
    for i in range(3):
        for j in range(3):
            if i != j:
                new = list(jars)
                transfer = min(jars[i], CAP[j] - jars[j])
                if transfer > 0:
                    new[i] -= transfer
                    new[j] += transfer
                    neighbors.append((tuple(new), f"transferir {NAMES[i]} -> {NAMES[j]}"))

    return neighbors


def bfs(target_jar): #BFS (Breadth-First Search) -> busca em largura
    start = (0, 0, 0)
    queue = deque()
    queue.append((start, []))
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        # objetivo: jarro escolhido com 4L
        if state[target_jar] == 4:
            return path, state

        for next_state, action in get_neighbors(state):
            if next_state not in visited:
                queue.append((next_state, path + [(state, action, next_state)]))

    return None


# ===== EXECUÇÃO =====

TARGET_JAR = 2  # 0=x (45L), 1=y (30L), 2=z (11L)

result = bfs(TARGET_JAR)

if result:
    path, final_state = result

    print(f"Objetivo: obter 4L no jarro {NAMES[TARGET_JAR]}\n(x, y, z)\n")
    print("Sequência de ações:\n")

    for step, (before, action, after) in enumerate(path, 1):
        print(f"{step}. ({before[0]}, {before[1]}, {before[2]}) -- {action} --> ({after[0]}, {after[1]}, {after[2]})")

    print("\nEstado final:")
    print(f"({final_state[0]}, {final_state[1]}, {final_state[2]})")

else:
    print("Não encontrou solução")