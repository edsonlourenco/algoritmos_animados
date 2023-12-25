# Map Reduce

O MapReduce é um modelo de programação e uma estrutura de processamento de dados que é comumente associada à computação distribuída em grande escala. Ele foi popularizado pelo Google e é usado para processar grandes conjuntos de dados em clusters de computadores.

Embora o MapReduce seja frequentemente usado para tarefas de processamento de dados em larga escala, ele não é especificamente um algoritmo de ordenação. Em vez disso, o MapReduce é um paradigma que consiste em duas fases principais: a fase de Map e a fase de Reduce.

![Diagrama animado do Map Reduce](../computacao_distribuida/drawio/map-reduce.drawio.svg)

Basicamente para facilitar nossa compreensão um Map Reduce pode ser dividido em duas fases, sendo elas:

1. **Fase de Map:**
   - Nesta fase, os dados de entrada são divididos em partes menores e processados em paralelo por várias máquinas. Cada máquina aplica uma função de mapeamento aos dados, produzindo um conjunto intermediário de pares chave-valor.

2. **Fase de Reduce:**
   - Os resultados intermediários são agrupados com base nas chaves e passados para as funções de redução. Cada função de redução opera em um conjunto de dados associado a uma chave específica, produzindo assim o resultado final.

Embora o MapReduce seja aplicável a uma variedade de problemas, incluindo processamento de dados, pesquisa em grandes conjuntos de dados e contagem de palavras, ele não é diretamente vinculado a algoritmos de ordenação. No entanto, algoritmos de ordenação podem ser implementados usando o paradigma MapReduce, especialmente em cenários onde a ordenação precisa ser distribuída em vários nós de computação.

* [Veja aqui em programação Python como ficaria](../computacao_distribuida/src/python/algoritmo_map_reduce.py)
* [Veja aqui o Notebook Jupyter do mesmo código como ficaria](../computacao_distribuida/src/python/algoritmo_map_reduce.ipynb)
---