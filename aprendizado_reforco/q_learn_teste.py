import numpy as np

alpha = 0.1
gamma = 0.9

# estados
states = [(0,0), (0,1), (1,0), (1,1)]
state_to_idx = {s:i for i,s in enumerate(states)}

# ações: cima, baixo, esquerda, direita
actions = [0,1,2,3]

# Tabela Q
Q = np.zeros((4,4))

# função de transição
def step(state, action):
    x, y = state
    
    if action == 0:   # cima
        x = max(0, x-1)
    elif action == 1: # baixo
        x = min(1, x+1)
    elif action == 2: # esquerda
        y = max(0, y-1)
    elif action == 3: # direita
        y = min(1, y+1)
    
    new_state = (x,y)
    
    # recompensa
    if new_state == (1,1):
        reward = 1
    else:
        reward = 0
        
    return new_state, reward

# política determinística: direita depois baixo
def choose_action(state):
    x, y = state

    if y < 1:
        return 3  # direita
    else:
        return 1  # baixo

# impressão da tabela
def print_Q(step_num):
    print(f"\nIteração {step_num}")
    for s in states:
        idx = state_to_idx[s]
        print(f"Estado {s} -> {Q[idx]}")

state = (0,0)
step_num = 0

print("Q inicial:")
print_Q(step_num)

while state != (1,1):
    step_num += 1
    
    s_idx = state_to_idx[state]
    
    action = choose_action(state)
    
    new_state, reward = step(state, action)
    ns_idx = state_to_idx[new_state]
    
    # guarda valores antes da atualização
    old_value = Q[s_idx, action]
    max_next = np.max(Q[ns_idx])
    
    # atualização Q-learning
    Q[s_idx, action] = old_value + alpha * (
        reward + gamma * max_next - old_value
    )

    # PRINT DA FÓRMULA (igual ao seu estilo)
    print(f"\nQ[{s_idx}, {action}] = {old_value} + {alpha} * ({reward} + {gamma} * {max_next} - {old_value})")
    print(f"Resultado: Q[{s_idx}, {action}] = {Q[s_idx, action]}")
    
    # print da tabela
    print_Q(step_num)
    
    # próximo estado
    state = new_state
    print(f"indo para proximo estado: {state}")

print("\nEstado final alcançado:", state)