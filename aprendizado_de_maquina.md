# Aprendizado de máquina 

IA:
- GOFAI (Good Old-Fashioned Artificial Intelligence): sistemas baseados na manipulação explícita de símbolos e regras lógicas
    - Problemas de busca
    - Sistemas especialistas
- Aprendizado de Maquina: Sistemas em que o modelo é aprendido, utilizar métodos para que o conhecimento seja usado para inferir o modelo automaticamente, sem serem explicitamente programados para cada tarefa.
    - Aprendizado baseado em dados
        - supervisionado: há uma etapa de treinamento com os dados rotulados, modelos são treniando com dados de entrada e saida conhecidas, aprendendo a mapear entradas para respostas corretas
            - classificação: entrada -> classes
            - regressao: entrada -> numeros
            - transformacao: saida é uma manipulação em cima da entrada
        - não supervisionado: não ha treinamento, modelos recebem apenas as entradas e aprendem a encontrar padroes, agrupamentos ou estruturas ocultas
            - agrupamento: entrada -> grupos
                - alguns algoritmos pedem que a gente passe o numero de grupos outros fazem isso de maneira automatica
                - da uma centroide para cada grupo tambem que é um bom representande do gupo
            - redução de dimensionalidade: diminuir o numero de variaveis (dimensões de um conjunto de dados)
                - melhorar a visualizaçao de dados complexos
                - acelerar algoritmos de apendizado de maquina
            - detecção de anomalias: detecção de dados que diferente significamente da maioria dos dados 
            - deteccao de regras: 
        - semi supervisionado: combina uma pequena quantidade de dados rotulados com muitos não rotulados, aproveitando o aprendizado supervisionado para guiar e generalizar melhor com os dados não rotulados
    - Aprendizado baseado em comportamento
        - por reforço: um agente interage com um ambiente realizando ações e recebendo recompensas


Aprendizado de Maquina -> usado aplicações que não podem ser implementadas a mão -> reconhecimento de caracteres manuscritos, processamento de linguagem natual (PLN), visão computacional

precisão só vale em aprendizado supervisionado, não vale para o não supervisionado 

Para o aprendizado de maquina é preciso de dados estruturados

# Ciencia de dados

- Termos importantes:
    - IA: sistema com racionalidade (maximizar ganhos apartir de objetivos pré-definidos), racionalidade diz respeito apenas as quais decisões são tomados (não ao pensamento que levou a decisão)
    - Mineração de dados: Vai estudar a parte de aprendizado de máquina e visualisação de dados (relatórios, graficos, ...)
    - Ciência de dados: O estudo dos dados em sí (coleta, seleção, pré-processamento, extração de caracteristicas, armazenamento) e a visualisação de dados (relatórios, graficos, ...)
    - Aprendizado de maquina:Sistemas em que o modelo é aprendido, utilizar métodos para que o conhecimento seja usado para inferir o modelo automaticamente, sem serem explicitamente programados para cada tarefa.

- Caracteristicas: atributos mensuraveis e com valor
    - tipos:
        - simbolicos ou qualitativos:
            - nominal ou categorigo: tipo de string que n é possivel estabelecer ordem (cor, código de identificação, profissão)
            - ordinal: tipo de string que pode colocar ordem (ex: gosto - ruim, médio, bom ; dias da semana)
        - numericos, continuos ou quantitativos: data e hora, real (temperatura, peos, tamanho), inteiro

- Problemas nos dados: falha humana, má fé, falha no processo de coleta/medição
    - como resolver:
        - valores ausentes:
            - descartar: descartar objetos com atributos sem valores (valido apenas se não for uma quantidade que prejudicaria significamente a aplicação)
            - substituir: substituir o valor por
                - média dos valores do atributo
                - média dos valores anterior e posterior
        - codificação: muitos algoritmos n conseguem trabalhar com string apenas numeros. Precisamos manter a ordem se houver e não criar ordem se não houver
            - para valores com ordem podemos simplesmente: ruim: 0, médio: 1, bom: 2
            - para valores sem ordem: one hot enconding -> para cada valor que o atributo pode assumir criar uma nova coluna, se o objeto tiver um valor colocar 1 na coluna que ele tem e 0 na que eles não tem
                - problema: quanto mais valores pode assumir, maior a tabela, mais memória ocupa
        - normalização: alguns algoritmos podem pedir a normalização, que é pegar os atributos e deixar em um intervalo especifico mantendo sua destribuição. Isso é util pois alguns algoritmos podem dar um peso maior para valores maiores (ex: peso é 4000g e altura 40cm, em alguns casos matematicamente nas contas o que pode ter mais peso nas contra seria o 'peso')
        - padronização (normalização Z): alguns algortimos exigem a transformação dos dados para que eles tenham média zero e desvio padrão 1, faz com que as caracteristicas tem a mesma esca e estejam centradas em 0

- Seleção e extração de caracteristicas: nem sempre pegar todas as caracteristicas vale a pena
    - ex: classificação de peixe entre ROBALO e SALMÃO
        - que caracteristicas podem ser validas para extrair?
            - comprimento
            - luminosidade 
            - numero de nadadeiras
            - forma das nadadeiras
        - fazer histogramas para visualisar as caracteristicas em relação as classes, isso pode mostrar se a caracteristica é boa para ser usada
        