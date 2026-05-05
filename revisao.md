inteligencia artificial: sistema com racionalidade (maximizar ganhos apartir de objetivos pré-definidos), racionalidade diz respeito apenas as quais decisões são tomados (não ao pensamento que levou a decisão)

modelos: 
    - mapeamento (todo modelo é uma representação de algo no mundo real)
    - pragmatismo (caracteristica que em alguns casos podemos substituir o objeto real pelo modelo) 
    - redução (nem todas as caracteristicas do modelo real as vezes podem ser convertidas para o modelo) 

paradigmas da IA:
    - simbolico: regras lógicas -> sistemas especialistas, vantagem é que pode ser explicado importante as vezes por questão de legislaçcão
    - conexionista: redes neurais -> nem todo problema pode ser resolvido com o simbolico, algumas coisas não podem ser transformadas em regras lógicas de maneira facil
    - evolutiva
    - probabilistica
    - hibrida
    - obs: busca n faz parte de nenhum deles

problemas de busca:
    - como modelar: 
        - conjunto de estados
        - estado inicial
        - estado final
        - conjunto de açcões
        - modelo de transição
        - custo de caminho
    - como resolver: busca em grafo
        - cega: busca em profundidade, busca em largura, busca de custo uniforme (encontra melhor solução)
        - informados (euristica h(x) ):  Busca gulosa (só euristica) (não encontra necessariamente a melhor solução), A* (euriscita e custo) (se h(x) for admissivel e consistente a solução vai ser a melhor solução)
            - tem a função euristica (valor numerico que estimativa de quão próximo esta a solução) que vai ajudar em alguns algoritmos informados a resolver o problema
            - euristica é admissivel quando
            - euristica é consistente quando

sistemas especialistas:
    - especialista cadastra regras (se então) na base de conhecimento
    - usuario insere fatos que são usados pelo motor de inferencia
    - encadeamento para frente usuario passa algumas informações iniciais: e checa todas conclusões que podem ser tiradas (tem q iterar até parar de ter novos fatos)
    - encadeamento para tras usuario passa fatos iniciais e uma conclusão: e checa se a partir desses fatos pode-se checar nessa conclusão (saindo da conclusão e voltando as regras)
    - partição fuzzy pode ser usada em sistemas esppecialistas:
        - insere dois modulos antes do motor de inferencia: o fuzzificador e deffuzificador (ver o slide depois)
        - fuzzificador pega os fatos e checa nos graficos os conjuntos, esses conjuntos são mandados pro motor de inferencia
            - e: conclusão pega o minimo
            - ou: conclusão pega o maximo
        - deffuzificador:
            - transforma em um unico valor numerico: soma da area nos graficos (ver o slide)
        - graficos que com base nos dados pode ser checado em qual dos conjuntos cai (não é 0 e 1, pode ter por ex 70% em um conjunto e 30% em outro conjunto)

aprendizado por reforço: tipo de aprendizado de maquina que foca na tomada de decisões por agentes autonomos
    - cai dentro do evolutivo mas para a prova lembrar só do conxionista e simbolico
    - procurar melhor no slide
    - um agente autonomo é qualquer sistema que pode tomar decisões e agir ao seu ambiente
    - toma a decisão baseado na recompensa acumulada
    - dois algoritmos:
        - Q - learning: tabela Q 
        - Baseado em politica: tabela pi -> probabilidades de tomar uma ação

na prova questaão de fuzzy vai bater na linha do grafico, n vai cair em valor intermediarios

avaliação vai ser na sala O202
prova vai ter 6 questões: algumas demoradas e outras não
tem uma questão de dasafio: não precisa fazer se não quiser, vale 1,5 a mais se acertar, se errar -0,5