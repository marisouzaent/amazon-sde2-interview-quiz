# -*- coding: utf-8 -*-
"""
Banco de perguntas do Quiz de preparação para entrevistas SDE-II (Amazon).

Cada pergunta é um dicionário com a seguinte estrutura:
{
    "id": str                -> identificador único da pergunta
    "type": "mcq" | "code"   -> "mcq" = conceitual, "code" = depuração de código
    "question": str          -> enunciado
    "code": str | None       -> snippet de código (opcional, usado em perguntas "code")
    "options": list[str]     -> alternativas
    "answer": int            -> índice (0-based) da alternativa correta
    "explanation": str       -> justificativa técnica da resposta
    "big_o": str             -> nota de complexidade (Big O) relacionada
}
"""

MODULES = {
    "arrays_hashing": {
        "title": "📊 Arrays, Hash Tables e Hashing",
        "icon": "📊",
        "description": (
            "Foco em identificar soluções de força bruta O(N²) e otimizá-las para "
            "O(N) usando tabelas de hash (dicionários/sets) para troca de tempo por espaço."
        ),
        "questions": [
            {
                "id": "arr_1",
                "type": "mcq",
                "question": (
                    "No problema clássico 'Two Sum', a abordagem de força bruta usa dois "
                    "laços aninhados para testar todos os pares possíveis. Qual é a "
                    "complexidade de tempo dessa abordagem?"
                ),
                "code": None,
                "options": ["O(1)", "O(N)", "O(N log N)", "O(N²)"],
                "answer": 3,
                "explanation": (
                    "Para cada um dos N elementos, o laço interno percorre novamente até N "
                    "elementos para encontrar o complemento, resultando em N × N comparações "
                    "no pior caso."
                ),
                "big_o": "Força bruta: O(N²) tempo, O(1) espaço.",
            },
            {
                "id": "arr_2",
                "type": "code",
                "question": (
                    "O código abaixo verifica duplicatas em um array com complexidade O(N²). "
                    "Qual mudança reduz a complexidade para O(N)?"
                ),
                "code": (
                    "def tem_duplicata(nums):\n"
                    "    for i in range(len(nums)):\n"
                    "        for j in range(i + 1, len(nums)):\n"
                    "            if nums[i] == nums[j]:\n"
                    "                return True\n"
                    "    return False"
                ),
                "options": [
                    "Ordenar o array antes de comparar (O(N log N) + O(N))",
                    "Usar um set para registrar elementos já vistos e checar pertencimento em O(1) médio",
                    "Trocar o laço interno por uma busca binária",
                    "Usar recursão para percorrer os pares",
                ],
                "answer": 1,
                "explanation": (
                    "Um set oferece inserção e busca em O(1) médio. Ao percorrer o array uma "
                    "única vez e checar 'if nums[i] in vistos', a complexidade cai de O(N²) "
                    "para O(N) tempo, ao custo de O(N) espaço extra — a clássica troca "
                    "tempo-por-espaço usando hashing."
                ),
                "big_o": "Solução com set/dict: O(N) tempo, O(N) espaço.",
            },
            {
                "id": "arr_3",
                "type": "mcq",
                "question": (
                    "Por que a busca por uma chave em um dicionário (hash table) do Python "
                    "é considerada O(1) em média, mas O(N) no pior caso?"
                ),
                "code": None,
                "options": [
                    "Porque o Python sempre converte o dicionário em lista antes de buscar",
                    "Porque colisões de hash podem degenerar buckets em listas encadeadas, exigindo varredura linear no pior caso",
                    "Porque dicionários são implementados como árvores binárias balanceadas",
                    "Porque a busca depende do tamanho das chaves, não da tabela",
                ],
                "answer": 1,
                "explanation": (
                    "A função de hash distribui as chaves em buckets. Em média, cada bucket "
                    "tem poucos elementos (O(1)). Porém, se muitas chaves colidirem no mesmo "
                    "bucket (pior caso), a busca degenera para varredura linear O(N)."
                ),
                "big_o": "Hash table: O(1) médio, O(N) pior caso.",
            },
            {
                "id": "arr_4",
                "type": "code",
                "question": (
                    "O código abaixo tenta comparar cada elemento com o próximo. Qual é o "
                    "problema técnico deste trecho?"
                ),
                "code": (
                    "def tem_par_igual(arr):\n"
                    "    for i in range(len(arr)):\n"
                    "        if arr[i] == arr[i + 1]:\n"
                    "            return True\n"
                    "    return False"
                ),
                "options": [
                    "Nenhum problema, o código está correto",
                    "IndexError: estouro de índice (off-by-one) na última iteração, pois arr[i+1] não existe quando i == len(arr)-1",
                    "O código tem complexidade O(N²) desnecessária",
                    "O laço nunca é executado",
                ],
                "answer": 1,
                "explanation": (
                    "Quando i assume o valor len(arr)-1 (último índice válido), a expressão "
                    "arr[i+1] tenta acessar um índice fora dos limites do array, lançando "
                    "IndexError. A correção é usar range(len(arr) - 1) ou validar "
                    "'i + 1 < len(arr)' antes do acesso."
                ),
                "big_o": "Bug de limite de índice, não é um problema de Big O, mas de correção.",
            },
            {
                "id": "arr_5",
                "type": "mcq",
                "question": (
                    "Para contar a frequência de elementos em um array de tamanho N, qual "
                    "estrutura/abordagem fornece a melhor complexidade de tempo?"
                ),
                "code": None,
                "options": [
                    "Percorrer o array e, para cada elemento, contar ocorrências com outro laço (O(N²))",
                    "Usar collections.Counter ou um dicionário para contar em uma única varredura (O(N))",
                    "Ordenar o array primeiro e depois buscar frequência com busca binária por elemento (O(N log N) + O(N log N))",
                    "Usar duas listas aninhadas para comparar todos os pares",
                ],
                "answer": 1,
                "explanation": (
                    "Um dicionário/Counter permite incrementar a contagem de cada elemento em "
                    "O(1) amortizado por operação, resultando em uma única varredura O(N) no "
                    "total — a melhor complexidade possível, já que é necessário olhar cada "
                    "elemento ao menos uma vez."
                ),
                "big_o": "Counter/dict: O(N) tempo, O(N) espaço no pior caso.",
            },
        ],
    },
    "linked_lists": {
        "title": "🔗 Linked Lists, Stacks e Queues",
        "icon": "🔗",
        "description": (
            "Foco em manipulação correta de ponteiros (next/prev), e na diferença de "
            "comportamento entre pilhas (LIFO) e filas (FIFO)."
        ),
        "questions": [
            {
                "id": "ll_1",
                "type": "mcq",
                "question": (
                    "Ao inverter uma lista encadeada simples de forma iterativa, quantos "
                    "ponteiros auxiliares são tipicamente necessários para evitar perder a "
                    "referência ao restante da lista?"
                ),
                "code": None,
                "options": [
                    "Nenhum, basta reatribuir node.next = node.prev",
                    "Um ponteiro (apenas 'current')",
                    "Três ponteiros: 'prev', 'current' e 'next_temp'",
                    "É necessário converter a lista em array primeiro",
                ],
                "answer": 2,
                "explanation": (
                    "Antes de redirecionar current.next para prev, é preciso guardar a "
                    "referência ao próximo nó em uma variável temporária (next_temp). Sem "
                    "isso, o restante da lista é perdido assim que o ponteiro é sobrescrito."
                ),
                "big_o": "Inversão iterativa: O(N) tempo, O(1) espaço.",
            },
            {
                "id": "ll_2",
                "type": "code",
                "question": (
                    "O código abaixo tenta inverter uma lista encadeada, mas contém um bug "
                    "clássico de manipulação de ponteiros. Qual é o problema?"
                ),
                "code": (
                    "def inverter(head):\n"
                    "    prev = None\n"
                    "    current = head\n"
                    "    while current is not None:\n"
                    "        current.next = prev\n"
                    "        prev = current\n"
                    "        current = current.next  # BUG\n"
                    "    return prev"
                ),
                "options": [
                    "O código está correto e inverte a lista normalmente",
                    "A linha 'current = current.next' lê o next DEPOIS de já ter sido sobrescrito para 'prev', perdendo o restante da lista (o laço termina cedo demais ou entra em ciclo)",
                    "O problema é que 'prev' deveria iniciar como uma lista vazia, não None",
                    "Falta uma recursão para percorrer a lista corretamente",
                ],
                "answer": 1,
                "explanation": (
                    "A ordem das operações importa: 'current.next = prev' sobrescreve o "
                    "ponteiro original para o próximo nó. Ao executar depois "
                    "'current = current.next', o código está lendo o valor já modificado "
                    "(que agora aponta para 'prev'), e não o nó seguinte original. É "
                    "necessário salvar 'next_temp = current.next' ANTES de sobrescrever."
                ),
                "big_o": "Bug de ordem de atribuição de ponteiros mutáveis — causa perda de dados, não afeta Big O diretamente.",
            },
            {
                "id": "ll_3",
                "type": "mcq",
                "question": (
                    "Qual estrutura de dados segue a disciplina LIFO (Last In, First Out) e "
                    "é comumente usada para validar parênteses balanceados?"
                ),
                "code": None,
                "options": ["Fila (Queue)", "Pilha (Stack)", "Árvore binária", "Grafo direcionado"],
                "answer": 1,
                "explanation": (
                    "A pilha (Stack) remove sempre o último elemento inserido. Em Python, "
                    "list.append()/list.pop() implementam uma pilha com O(1) amortizado por "
                    "operação, ideal para rastrear parênteses abertos aguardando fechamento."
                ),
                "big_o": "Push/Pop em pilha (lista Python): O(1) amortizado.",
            },
            {
                "id": "ll_4",
                "type": "mcq",
                "question": (
                    "Por que usar list.pop(0) repetidamente para implementar uma fila (FIFO) "
                    "em Python é uma má prática de performance?"
                ),
                "code": None,
                "options": [
                    "Porque list.pop(0) é O(N), já que todos os elementos restantes precisam ser deslocados uma posição; o ideal é usar collections.deque com popleft() em O(1)",
                    "Porque listas não suportam remoção de elementos",
                    "Porque pop(0) lança uma exceção em listas vazias apenas em Python 3",
                    "Não há problema, pop(0) já é O(1) internamente",
                ],
                "answer": 0,
                "explanation": (
                    "Listas em Python são implementadas como arrays dinâmicos. Remover o "
                    "primeiro elemento exige deslocar todos os N-1 elementos restantes, "
                    "custando O(N). collections.deque é implementado como uma lista "
                    "duplamente encadeada de blocos, permitindo popleft()/appendleft() em "
                    "O(1)."
                ),
                "big_o": "list.pop(0): O(N); deque.popleft(): O(1).",
            },
            {
                "id": "ll_5",
                "type": "code",
                "question": (
                    "O código abaixo tenta detectar um ciclo em uma lista encadeada usando o "
                    "algoritmo de Floyd (tortoise and hare), mas tem um bug. Qual é o problema?"
                ),
                "code": (
                    "def tem_ciclo(head):\n"
                    "    slow = head\n"
                    "    fast = head\n"
                    "    while fast is not None:\n"
                    "        slow = slow.next\n"
                    "        fast = fast.next  # BUG: deveria avançar 2 posições\n"
                    "        if slow == fast:\n"
                    "            return True\n"
                    "    return False"
                ),
                "options": [
                    "O código está correto, pois ambos os ponteiros devem andar na mesma velocidade",
                    "O ponteiro 'fast' deveria avançar duas posições (fast.next.next) a cada iteração; se avançar apenas uma, o algoritmo nunca detecta o ciclo mais rápido e pode entrar em loop infinito, já que 'fast' nunca se torna None em uma lista cíclica",
                    "O ponteiro 'slow' é que está incorreto",
                    "Falta inicializar slow e fast com valores diferentes",
                ],
                "answer": 1,
                "explanation": (
                    "A essência do algoritmo de Floyd é a diferença de velocidade: 'slow' "
                    "anda 1 passo e 'fast' anda 2 passos por iteração. Se ambos andarem na "
                    "mesma velocidade, slow == fast sempre será verdadeiro (são o mesmo nó), "
                    "ou, em uma lista com ciclo real, 'fast' nunca encontra a condição de "
                    "parada 'fast is None', gerando um loop infinito sem necessariamente "
                    "chegar à detecção correta."
                ),
                "big_o": "Detecção de ciclo (Floyd): O(N) tempo, O(1) espaço — superior a usar um set de nós visitados (O(N) espaço).",
            },
        ],
    },
    "trees_bst": {
        "title": "🌳 Trees e Binary Search Trees (BST)",
        "icon": "🌳",
        "description": (
            "Foco em casos base de recursão e na armadilha clássica de validar uma BST "
            "comparando apenas com o pai imediato, em vez de usar limites (min/max)."
        ),
        "questions": [
            {
                "id": "tree_1",
                "type": "mcq",
                "question": (
                    "Em uma travessia recursiva de árvore (in-order, pre-order ou post-order), "
                    "qual é o caso base indispensável para evitar recursão infinita?"
                ),
                "code": None,
                "options": [
                    "if node.value == 0: return",
                    "if node is None: return",
                    "if node.left is None and node.right is None: return",
                    "Não existe caso base necessário em árvores",
                ],
                "answer": 1,
                "explanation": (
                    "Toda recursão sobre árvores deve parar ao atingir um nó nulo (folha "
                    "além do limite da árvore). Sem 'if node is None: return', a recursão "
                    "tentaria acessar atributos de None, lançando AttributeError, ou nunca "
                    "terminaria em estruturas malformadas."
                ),
                "big_o": "Travessias de árvore: O(N) tempo (visita cada nó uma vez), O(H) espaço de pilha de recursão (H = altura).",
            },
            {
                "id": "tree_2",
                "type": "code",
                "question": (
                    "O código abaixo tenta validar se uma árvore é uma BST válida, mas "
                    "contém a armadilha mais comum desse problema. Qual é o bug?"
                ),
                "code": (
                    "def eh_bst_valida(node):\n"
                    "    if node is None:\n"
                    "        return True\n"
                    "    if node.left and node.left.val >= node.val:\n"
                    "        return False\n"
                    "    if node.right and node.right.val <= node.val:\n"
                    "        return False\n"
                    "    return eh_bst_valida(node.left) and eh_bst_valida(node.right)"
                ),
                "options": [
                    "O código está correto, comparar com os filhos imediatos é suficiente",
                    "O código só compara cada nó com seus filhos diretos, ignorando a regra de que TODOS os nós da subárvore esquerda devem ser menores e da direita maiores que ancestrais mais distantes — é preciso propagar limites (min, max) pela recursão",
                    "Falta inverter as comparações (>= deveria ser <=)",
                    "O problema é que a função deveria ser iterativa, não recursiva",
                ],
                "answer": 1,
                "explanation": (
                    "Uma BST exige que TODO nó na subárvore esquerda de um ancestral seja "
                    "menor que esse ancestral (não apenas que o pai imediato). Comparar "
                    "apenas com o pai direto permite árvores inválidas passarem, como um nó "
                    "neto à esquerda com valor maior que o avô. A solução correta propaga "
                    "limites (low, high) recursivamente: "
                    "validar(node, low, high) -> low < node.val < high."
                ),
                "big_o": "Validação correta de BST com limites: O(N) tempo, O(H) espaço — mesma complexidade da versão com bug, mas com corretude garantida.",
            },
            {
                "id": "tree_3",
                "type": "mcq",
                "question": (
                    "Qual é a complexidade de tempo para buscar um valor em uma BST "
                    "balanceada versus uma BST completamente degenerada (desbalanceada, como "
                    "uma lista encadeada)?"
                ),
                "code": None,
                "options": [
                    "O(log N) balanceada e O(N) degenerada",
                    "O(N) em ambos os casos",
                    "O(1) balanceada e O(log N) degenerada",
                    "O(log N) em ambos os casos, pois é sempre uma árvore",
                ],
                "answer": 0,
                "explanation": (
                    "Em uma BST balanceada, cada comparação elimina metade dos nós "
                    "restantes, resultando em O(log N) (altura ~ log N). Se a árvore "
                    "degenerar (ex.: inserir elementos já ordenados sem balanceamento), ela "
                    "vira efetivamente uma lista encadeada com altura N, tornando a busca "
                    "O(N)."
                ),
                "big_o": "BST balanceada: O(log N). BST degenerada: O(N).",
            },
            {
                "id": "tree_4",
                "type": "mcq",
                "question": (
                    "Qual tipo de travessia de uma BST válida sempre retorna os elementos em "
                    "ordem crescente?"
                ),
                "code": None,
                "options": ["Pre-order", "Post-order", "In-order", "Level-order (BFS)"],
                "answer": 2,
                "explanation": (
                    "A travessia in-order (esquerda, raiz, direita) visita os nós na ordem "
                    "crescente de valores em uma BST válida, pois respeita a propriedade de "
                    "que a subárvore esquerda contém valores menores e a direita, maiores."
                ),
                "big_o": "In-order traversal: O(N) tempo, O(H) espaço de recursão.",
            },
            {
                "id": "tree_5",
                "type": "code",
                "question": (
                    "O código abaixo calcula a altura de uma árvore, mas foi escrito sem um "
                    "caso base. Qual é a consequência técnica desse erro?"
                ),
                "code": (
                    "def altura(node):\n"
                    "    # BUG: falta 'if node is None: return -1' ou similar\n"
                    "    return 1 + max(altura(node.left), altura(node.right))"
                ),
                "options": [
                    "O código funciona normalmente, apenas é um pouco mais lento",
                    "Sem caso base, a recursão nunca para ao atingir um filho nulo, resultando em AttributeError (acessar .left/.right de None) ou RecursionError por estouro de pilha",
                    "O código retorna sempre 0, independentemente da árvore",
                    "O código funciona, mas calcula a altura errada em 1 unidade"
                ],
                "answer": 1,
                "explanation": (
                    "Toda função recursiva sobre árvores precisa de uma condição de parada "
                    "para nós nulos. Sem ela, ao alcançar uma folha, a chamada "
                    "altura(node.left) tentará acessar atributos de um objeto None, "
                    "lançando AttributeError, ou, dependendo da implementação, levará a uma "
                    "recursão sem fim até estourar o limite de profundidade da pilha "
                    "(RecursionError)."
                ),
                "big_o": "Cálculo de altura (correto): O(N) tempo, O(H) espaço de pilha.",
            },
        ],
    },
    "graphs_bfs_dfs": {
        "title": "🕸️ Grafos, BFS e DFS",
        "icon": "🕸️",
        "description": (
            "Foco em travessias de matrizes 2D (grids), marcação correta de nós visitados "
            "para evitar reprocessamento ou loops infinitos."
        ),
        "questions": [
            {
                "id": "graph_1",
                "type": "mcq",
                "question": (
                    "Qual estrutura de dados é utilizada pelo BFS (Busca em Largura) para "
                    "garantir que os nós sejam visitados em ordem de distância crescente a "
                    "partir da origem?"
                ),
                "code": None,
                "options": ["Pilha (Stack)", "Fila (Queue)", "Heap de máximo", "Lista ligada circular"],
                "answer": 1,
                "explanation": (
                    "BFS usa uma fila (FIFO): o primeiro nó a ser adicionado é o primeiro a "
                    "ser processado, garantindo que todos os nós a distância K sejam "
                    "visitados antes de qualquer nó a distância K+1. Isso torna o BFS ideal "
                    "para encontrar o caminho mais curto em grafos não ponderados."
                ),
                "big_o": "BFS: O(V + E) tempo, onde V = vértices e E = arestas.",
            },
            {
                "id": "graph_2",
                "type": "mcq",
                "question": (
                    "O DFS (Busca em Profundidade) pode ser implementado de duas formas "
                    "equivalentes. Quais são elas?"
                ),
                "code": None,
                "options": [
                    "Apenas com fila (queue)",
                    "Recursão (usando a pilha de chamadas implícita) ou uma pilha (stack) explícita iterativa",
                    "Apenas com uma matriz de adjacência",
                    "DFS só pode ser implementado de forma recursiva",
                ],
                "answer": 1,
                "explanation": (
                    "DFS explora o mais fundo possível antes de retroceder (backtrack). Isso "
                    "pode ser feito com recursão (a própria pilha de chamadas da linguagem "
                    "atua como a pilha de exploração) ou de forma iterativa usando uma pilha "
                    "explícita (list.append/pop)."
                ),
                "big_o": "DFS: O(V + E) tempo, O(V) espaço no pior caso (pilha de recursão/estrutura explícita).",
            },
            {
                "id": "graph_3",
                "type": "code",
                "question": (
                    "O código abaixo resolve 'Number of Islands' em uma matriz 2D com BFS, "
                    "mas contém um bug clássico de marcação de visitados. Qual é o problema?"
                ),
                "code": (
                    "from collections import deque\n\n"
                    "def bfs(grid, r, c, visitado):\n"
                    "    fila = deque([(r, c)])\n"
                    "    while fila:\n"
                    "        row, col = fila.popleft()\n"
                    "        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:\n"
                    "            nr, nc = row + dr, col + dc\n"
                    "            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):\n"
                    "                if grid[nr][nc] == '1' and (nr, nc) not in visitado:\n"
                    "                    fila.append((nr, nc))\n"
                    "                    # BUG: visitado só é marcado ao desenfileirar, não aqui"
                ),
                "options": [
                    "O código está correto, não há problema algum",
                    "O nó é marcado como visitado apenas quando é desenfileirado (ou nunca, neste trecho), permitindo que a mesma célula seja adicionada várias vezes à fila antes de ser processada — isso causa processamento duplicado e, em grids grandes, explosão de memória/tempo",
                    "A fila deveria ser substituída por uma pilha para funcionar corretamente",
                    "O problema é usar tuplas como coordenadas em vez de listas",
                ],
                "answer": 1,
                "explanation": (
                    "A regra de ouro do BFS/DFS em grids é: marque como visitado NO MOMENTO "
                    "em que o nó é enfileirado/adicionado à pilha, não apenas quando é "
                    "processado. Caso contrário, múltiplos vizinhos podem enfileirar a mesma "
                    "célula antes que ela seja marcada, causando reprocessamento redundante "
                    "e, em casos extremos, estouro de memória ou tempo de execução muito "
                    "acima do O(linhas × colunas) esperado."
                ),
                "big_o": "BFS/DFS em grid correto: O(linhas × colunas) tempo e espaço.",
            },
            {
                "id": "graph_4",
                "type": "mcq",
                "question": (
                    "Qual é a complexidade de tempo esperada para percorrer completamente "
                    "(BFS ou DFS) uma matriz 2D (grid) de dimensões R linhas por C colunas, "
                    "marcando corretamente os nós visitados?"
                ),
                "code": None,
                "options": ["O(R + C)", "O(R × C)", "O(log(R × C))", "O((R × C)²)"],
                "answer": 1,
                "explanation": (
                    "Cada célula do grid é visitada e processada no máximo uma vez (graças à "
                    "marcação de visitados), e cada célula tem até 4 vizinhos verificados em "
                    "tempo constante. Logo, o trabalho total é proporcional ao número total "
                    "de células: O(R × C)."
                ),
                "big_o": "Travessia completa de grid: O(R × C) tempo, O(R × C) espaço (visitados + fila/pilha no pior caso).",
            },
            {
                "id": "graph_5",
                "type": "code",
                "question": (
                    "O código abaixo verifica os vizinhos de uma célula em um grid, mas "
                    "pode lançar uma exceção em tempo de execução. Qual é o problema?"
                ),
                "code": (
                    "def vizinho_e_terra(grid, r, c):\n"
                    "    # BUG: não valida limites antes de acessar grid[r][c]\n"
                    "    return grid[r][c] == '1'\n\n"
                    "def explorar(grid, r, c):\n"
                    "    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:\n"
                    "        if vizinho_e_terra(grid, r + dr, c + dc):\n"
                    "            print('terra encontrada')"
                ),
                "options": [
                    "O código está correto para qualquer grid",
                    "Faltam checagens de limite (0 <= r < num_linhas e 0 <= c < num_colunas) antes de acessar grid[r][c], causando IndexError quando a célula vizinha está fora da borda da matriz",
                    "O problema é usar uma lista de tuplas para as direções",
                    "A função deveria retornar None em vez de um booleano",
                ],
                "answer": 1,
                "explanation": (
                    "Ao explorar vizinhos nas bordas do grid (ex.: r=0 e dr=-1 resulta em "
                    "r=-1), o acesso direto grid[r][c] pode causar IndexError (índice fora "
                    "do intervalo) ou, pior, acessar silenciosamente o final do array via "
                    "índices negativos do Python (grid[-1] é válido!), retornando dados "
                    "incorretos sem lançar erro. A correção exige validar explicitamente "
                    "'0 <= r < len(grid) and 0 <= c < len(grid[0])' antes do acesso."
                ),
                "big_o": "Checagem de limites: O(1) por vizinho — custo constante, mas evita corrupção lógica silenciosa.",
            },
        ],
    },
    "binary_search_sorting": {
        "title": "🔍 Busca Binária e Ordenação",
        "icon": "🔍",
        "description": (
            "Foco na complexidade O(log N) da busca binária, pré-condições (array "
            "ordenado) e armadilhas de atualização de ponteiros que causam loops infinitos."
        ),
        "questions": [
            {
                "id": "bs_1",
                "type": "mcq",
                "question": (
                    "Qual é a pré-condição obrigatória para que a busca binária funcione "
                    "corretamente, e qual sua complexidade de tempo?"
                ),
                "code": None,
                "options": [
                    "O array deve estar ordenado; complexidade O(log N)",
                    "O array pode estar em qualquer ordem; complexidade O(log N)",
                    "O array deve estar ordenado; complexidade O(N)",
                    "Não há pré-condição; complexidade O(1)",
                ],
                "answer": 0,
                "explanation": (
                    "A busca binária depende de poder descartar metade do espaço de busca a "
                    "cada iteração, comparando o valor do meio com o alvo. Isso só é válido "
                    "se o array estiver ordenado. A cada comparação, o espaço de busca é "
                    "dividido por 2, resultando em O(log N) iterações no total."
                ),
                "big_o": "Busca binária: O(log N) tempo, O(1) espaço (versão iterativa).",
            },
            {
                "id": "bs_2",
                "type": "code",
                "question": (
                    "O código de busca binária abaixo contém um bug que causa loop infinito "
                    "em certos casos. Qual é o problema?"
                ),
                "code": (
                    "def busca_binaria(arr, alvo):\n"
                    "    low, high = 0, len(arr) - 1\n"
                    "    while low <= high:\n"
                    "        mid = (low + high) // 2\n"
                    "        if arr[mid] < alvo:\n"
                    "            low = mid  # BUG: deveria ser mid + 1\n"
                    "        elif arr[mid] > alvo:\n"
                    "            high = mid - 1\n"
                    "        else:\n"
                    "            return mid\n"
                    "    return -1"
                ),
                "options": [
                    "O código está correto e nunca entra em loop infinito",
                    "Ao fazer 'low = mid' em vez de 'low = mid + 1', quando low e high convergem para o mesmo índice (high - low == 1 e mid == low), o intervalo nunca se reduz, mantendo 'mid' preso no mesmo valor indefinidamente",
                    "O problema está na condição 'arr[mid] > alvo', que deveria ser '>='",
                    "A variável 'mid' deveria ser calculada com multiplicação em vez de divisão",
                ],
                "answer": 1,
                "explanation": (
                    "Para garantir que o espaço de busca sempre diminua, ao descartar a "
                    "metade inferior é preciso avançar 'low' para 'mid + 1' (excluindo o "
                    "índice já testado). Ao manter 'low = mid', existe um cenário em que "
                    "mid == low (ex.: low=3, high=4, mid=3) e a condição 'arr[mid] < alvo' "
                    "permanece verdadeira indefinidamente, pois low nunca ultrapassa high — "
                    "resultando em um loop infinito."
                ),
                "big_o": "Busca binária correta: O(log N). Com o bug: loop infinito (complexidade não definida / trava o programa).",
            },
            {
                "id": "bs_3",
                "type": "mcq",
                "question": (
                    "Comparando algoritmos de ordenação, qual afirmação sobre complexidade é "
                    "correta?"
                ),
                "code": None,
                "options": [
                    "Quicksort tem complexidade garantida de O(N log N) em todos os casos, melhor que Merge Sort",
                    "Merge Sort garante O(N log N) no pior caso (às custas de O(N) de espaço extra), enquanto Quicksort tem O(N log N) médio mas pode degradar para O(N²) no pior caso (ex.: array já ordenado com pivô mal escolhido)",
                    "Bubble Sort é o algoritmo de ordenação mais eficiente para grandes volumes de dados, com O(N log N)",
                    "Todos os algoritmos de ordenação por comparação têm a mesma complexidade de O(N)",
                ],
                "answer": 1,
                "explanation": (
                    "Merge Sort divide o array e sempre mescla em tempo linear por nível, "
                    "garantindo O(N log N) estável, mas usa O(N) de memória auxiliar. "
                    "Quicksort é in-place (O(log N) de espaço em média) e O(N log N) em "
                    "média, mas a escolha ruim de pivô (ex.: sempre o primeiro elemento em "
                    "um array já ordenado) pode degradar para O(N²) no pior caso."
                ),
                "big_o": "Merge Sort: O(N log N) garantido, O(N) espaço. Quicksort: O(N log N) médio, O(N²) pior caso, O(log N) espaço.",
            },
            {
                "id": "bs_4",
                "type": "code",
                "question": (
                    "O código abaixo usa a condição 'low < high' em vez de 'low <= high' em "
                    "uma busca binária. Qual é a consequência prática dessa troca?"
                ),
                "code": (
                    "def busca_binaria(arr, alvo):\n"
                    "    low, high = 0, len(arr) - 1\n"
                    "    while low < high:  # BUG: deveria ser low <= high\n"
                    "        mid = (low + high) // 2\n"
                    "        if arr[mid] == alvo:\n"
                    "            return mid\n"
                    "        elif arr[mid] < alvo:\n"
                    "            low = mid + 1\n"
                    "        else:\n"
                    "            high = mid - 1\n"
                    "    return -1"
                ),
                "options": [
                    "Não há consequência, o comportamento é idêntico em todos os casos",
                    "Quando o intervalo se reduz a um único elemento (low == high), o laço não executa mais nenhuma iteração e esse último elemento nunca é comparado com o alvo, podendo retornar -1 incorretamente mesmo quando o alvo está presente nessa posição",
                    "O código entra em loop infinito sempre que o alvo não existe no array",
                    "A troca só afeta a complexidade, tornando-a O(N) em vez de O(log N)",
                ],
                "answer": 1,
                "explanation": (
                    "A condição 'low <= high' é necessária para garantir que o último "
                    "elemento candidato (quando low == high, um único elemento restante no "
                    "intervalo) seja de fato testado. Usar 'low < high' interrompe o laço "
                    "antes dessa checagem, criando um off-by-one error que pode gerar falso "
                    "negativo em arrays pequenos ou quando o alvo é o último candidato "
                    "restante no intervalo de busca."
                ),
                "big_o": "Complexidade permanece O(log N) em ambas as versões — o bug é de corretude (off-by-one), não de performance.",
            },
            {
                "id": "bs_5",
                "type": "mcq",
                "question": (
                    "Em qual cenário faz mais sentido usar busca binária (O(log N)) em vez "
                    "de busca linear (O(N))?"
                ),
                "code": None,
                "options": [
                    "Quando o array não está ordenado e muda constantemente de posição",
                    "Quando o array está ordenado (ou pode ser ordenado uma vez) e haverá muitas buscas subsequentes, amortizando o custo de ordenação",
                    "Quando o array tem menos de 3 elementos",
                    "Busca binária nunca é vantajosa em relação à busca linear",
                ],
                "answer": 1,
                "explanation": (
                    "Busca binária exige um array ordenado. Se os dados já estão ordenados "
                    "(ou serão ordenados uma única vez com custo O(N log N) e consultados "
                    "muitas vezes depois), cada busca subsequente custa O(log N) em vez de "
                    "O(N), uma economia significativa para N grande e múltiplas consultas. "
                    "Se o array muda constantemente e é consultado só uma vez, o custo de "
                    "reordenar pode não compensar."
                ),
                "big_o": "Busca linear: O(N). Busca binária: O(log N) após O(N log N) de ordenação inicial (amortizado em múltiplas buscas).",
            },
        ],
    },
}

# ------------------------------------------------------------------------------
# Exemplos Práticos Detalhados — Problema, Esqueleto e Solução Explicada
# ------------------------------------------------------------------------------
# Cada exemplo é um dicionário com a seguinte estrutura:
# {
#   "id": str                 -> identificador único
#   "title": str              -> título do exemplo (ex.: "Two Sum")
#   "pillar": str             -> pilar/tema coberto
#   "context": str            -> enunciado e contexto do problema
#   "skeleton_code": str      -> código incompleto para o usuário tentar resolver
#   "reasoning_prompt": str   -> pergunta que guia o raciocínio antes de ver a solução
#   "solution_code": str      -> código resolvido
#   "explanation": str        -> explicação de por que a solução funciona
#   "why_concept": str        -> justificativa de por que usar esse conceito/estrutura
# }
PRACTICAL_EXAMPLES = [
    {
        "id": "example_two_sum",
        "title": "Two Sum",
        "pillar": "🔑 Hash Tables & Arrays",
        "context": (
            "Dado um array de inteiros `nums` e um inteiro `target`, retorne os índices "
            "`i` e `j` tais que `nums[i] + nums[j] == target` e `i != j`."
        ),
        "skeleton_code": (
            "class Solution:\n"
            "    def twoSum(self, nums: List[int], target: int) -> List[int]:\n"
            "        # Escreva sua lógica aqui usando um dicionário (hash map)\n"
            "        # para otimizar a busca\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: qual estrutura de dados permite verificar em "
            "O(1) se o complemento de um número (target - nums[i]) já foi visto? Como você "
            "evitaria o loop duplo O(N²) da força bruta?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def twoSum(self, nums: List[int], target: int) -> List[int]:\n"
            "        prevMap = {}  # Mapeia valor -> índice (val -> index)\n"
            "\n"
            "        for i, n in enumerate(nums):\n"
            "            diff = target - n  # Calcula o complemento necessário\n"
            "            if diff in prevMap:\n"
            "                return [prevMap[diff], i]  # Retorna índice do complemento e o atual\n"
            "            prevMap[n] = i  # Armazena o número atual no mapa\n"
            "        return []"
        ),
        "explanation": (
            "A cada iteração, calculamos o complemento (`diff = target - n`) e verificamos "
            "se ele já foi visto antes, consultando o dicionário `prevMap`. Se sim, "
            "encontramos o par e retornamos os dois índices. Caso contrário, guardamos o "
            "número atual no dicionário para que futuras iterações possam encontrá-lo."
        ),
        "why_concept": (
            "O uso do Hash Map reduz a complexidade temporal de O(N²) (força bruta com dois "
            "loops) para O(N), pois a inserção e a busca no dicionário custam O(1) em média."
        ),
        "big_o": "Força bruta: O(N²) tempo. Com hash map: O(N) tempo, O(N) espaço.",
    },
    {
        "id": "example_valid_parentheses",
        "title": "Valid Parentheses",
        "pillar": "📚 Stacks",
        "context": (
            "Dada uma string `s` contendo caracteres de parênteses, colchetes e chaves, "
            "determine se a string é válida, garantindo que os pares abram e fechem na "
            "ordem correta."
        ),
        "skeleton_code": (
            "class Solution:\n"
            "    def isValid(self, s: str) -> bool:\n"
            "        # Utilize uma pilha (stack) e um dicionário de mapeamento\n"
            "        # de fechamento -> abertura\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: qual estrutura de dados segue o comportamento "
            "LIFO (último a entrar, primeiro a sair)? Como você decidiria, ao encontrar um "
            "caractere de fechamento, se ele corresponde à última abertura pendente?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def isValid(self, s: str) -> bool:\n"
            "        stack = []\n"
            "        closeToOpen = { \")\" : \"(\", \"]\" : \"[\", \"}\" : \"{\" }  # fechamento -> abertura\n"
            "\n"
            "        for c in s:\n"
            "            if c in closeToOpen:\n"
            "                # Verifica se a pilha não está vazia e o topo corresponde ao par\n"
            "                if stack and stack[-1] == closeToOpen[c]:\n"
            "                    stack.pop()\n"
            "                else:\n"
            "                    return False\n"
            "            else:\n"
            "                stack.append(c)  # Empilha caracteres de abertura\n"
            "\n"
            "        return True if not stack else False  # Pilha vazia = tudo fechou corretamente"
        ),
        "explanation": (
            "Percorremos a string caractere a caractere. Ao encontrar um caractere de "
            "abertura, empilhamos. Ao encontrar um de fechamento, comparamos com o topo da "
            "pilha: se corresponder ao par de abertura esperado, desempilhamos; caso "
            "contrário, a string é inválida. No final, a string só é válida se a pilha "
            "estiver completamente vazia (todas as aberturas foram fechadas)."
        ),
        "why_concept": (
            "O comportamento LIFO (Last In, First Out) da Pilha (Stack) é perfeito para "
            "gerenciar estruturas aninhadas, onde o elemento de abertura mais recente deve "
            "ser o primeiro a ser fechado."
        ),
        "big_o": "O(N) tempo, O(N) espaço no pior caso (string só com caracteres de abertura).",
    },
    {
        "id": "example_number_of_islands",
        "title": "Number of Islands",
        "pillar": "🌐 Grafos / DFS",
        "context": (
            "Dada uma grade 2D de `'1'`s (terra) e `'0'`s (água), conte e retorne o número "
            "de ilhas formadas por conexões horizontais ou verticais."
        ),
        "skeleton_code": (
            "class Solution:\n"
            "    def numIslands(self, grid: List[List[str]]) -> int:\n"
            "        # Implemente a travessia por DFS para \"afundar\" a ilha visitada\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: como você evitaria contar a mesma ilha mais de "
            "uma vez? Qual seria a condição de parada da sua busca em profundidade (DFS) ao "
            "explorar uma célula de terra?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def numIslands(self, grid: List[List[str]]) -> int:\n"
            "        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]\n"
            "        ROWS, COLS = len(grid), len(grid[0])\n"
            "        islands = 0\n"
            "\n"
            "        def dfs(r, c):\n"
            "            # Condição de parada: fora dos limites ou se for água ('0')\n"
            "            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == \"0\":\n"
            "                return\n"
            "\n"
            "            grid[r][c] = \"0\"  # Marca a célula atual como visitada (afunda a terra)\n"
            "            for dr, dc in directions:\n"
            "                dfs(r + dr, c + dc)  # Explora recursivamente as 4 direções\n"
            "\n"
            "        for r in range(ROWS):\n"
            "            for c in range(COLS):\n"
            "                if grid[r][c] == \"1\":\n"
            "                    dfs(r, c)  # Inicia a varredura da ilha\n"
            "                    islands += 1  # Incrementa o contador de ilhas\n"
            "\n"
            "        return islands"
        ),
        "explanation": (
            "Percorremos cada célula da grade. Ao encontrar terra (`'1'`) ainda não "
            "visitada, iniciamos uma DFS que marca toda a ilha conectada como água "
            "(`'0'`), evitando contagem duplicada, e incrementamos o contador de ilhas. "
            "A DFS para quando sai dos limites da grade ou encontra água."
        ),
        "why_concept": (
            "A Busca em Profundidade (DFS) combinada com a marcação in-place "
            "(`grid[r][c] = \"0\"`) garante que cada célula seja visitada de forma "
            "eficiente, sem entrar em loops infinitos por ciclos no grafo."
        ),
        "big_o": "O(R × C) tempo (cada célula visitada uma vez), O(R × C) espaço no pior caso (pilha de recursão).",
    },
    # --------------------------------------------------------------------
    # Cenários de Entrevista (simulação de raciocínio em voz alta)
    # --------------------------------------------------------------------
    # Além dos campos padrão, estes itens incluem:
    #   "clarifying_questions": list[str]  -> perguntas a fazer ao entrevistador
    #   "reasoning_script": str            -> script de raciocínio em 1ª pessoa,
    #                                          revelado junto com a solução
    {
        "id": "scenario_contains_duplicate",
        "title": "Otimização de Busca em Vetores (Contains Duplicate)",
        "pillar": "🔑 Hash Tables & Arrays",
        "context": (
            "O entrevistador pede para verificar se existem elementos duplicados em um "
            "array grande."
        ),
        "clarifying_questions": [
            "Os dados de entrada estão ordenados de alguma forma?",
            "Quais são as restrições de tamanho (constraints) do array e os limites de "
            "memória da aplicação?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def containsDuplicate(self, nums: List[int]) -> bool:\n"
            "        # Utilize um Hash Set para verificar duplicatas em O(1) por elemento\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: como você evitaria o loop duplo O(N²) da "
            "força bruta? Qual estrutura permite checar em O(1) se um valor já foi visto?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def containsDuplicate(self, nums: List[int]) -> bool:\n"
            "        seen = set()\n"
            "\n"
            "        for n in nums:\n"
            "            if n in seen:\n"
            "                return True  # Já vimos esse número antes\n"
            "            seen.add(n)\n"
            "\n"
            "        return False"
        ),
        "reasoning_script": (
            "\"A abordagem mais intuitiva seria usar dois loops aninhados para comparar "
            "cada elemento com os demais, mas isso resultaria em uma complexidade de tempo "
            "de O(N²), o que é ineficiente para grandes volumes de dados. Para otimizar "
            "isso para O(N), vou utilizar um Hash Set em Python. A ideia é iterar pela "
            "lista apenas uma vez: enquanto percorro, checo se o elemento atual já existe "
            "no nosso conjunto. Como as operações de inserção e busca em um Hash Set custam "
            "O(1) em média, conseguimos reduzir drasticamente o tempo de execução, pagando "
            "o trade-off de consumir O(N) de espaço extra na memória.\""
        ),
        "explanation": (
            "Percorremos o array uma única vez, guardando cada número em um `set`. Se um "
            "número já estiver no conjunto antes de ser adicionado, encontramos uma "
            "duplicata e retornamos `True` imediatamente."
        ),
        "why_concept": (
            "O Hash Set oferece inserção e busca O(1) em média, trocando espaço extra "
            "(O(N)) por uma redução de tempo de O(N²) para O(N) — um trade-off clássico "
            "de entrevistas técnicas."
        ),
        "big_o": "Força bruta: O(N²) tempo, O(1) espaço. Com hash set: O(N) tempo, O(N) espaço.",
    },
    {
        "id": "scenario_group_anagrams",
        "title": "Escolha de Chaves Imutáveis para Agrupamento (Group Anagrams)",
        "pillar": "🔑 Hash Tables & Arrays",
        "context": (
            "Agrupar itens com características semelhantes (palavras anagramas) "
            "utilizando mapas."
        ),
        "clarifying_questions": [
            "As strings contêm apenas letras minúsculas do alfabeto inglês ou podem "
            "incluir caracteres especiais, maiúsculas e acentos?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n"
            "        # Utilize uma chave 'hashable' derivada de cada string\n"
            "        # (ex.: tupla de contagem de letras) para agrupar anagramas\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: por que não podemos usar listas como chave "
            "de dicionário? Que chave 'hashable' representaria unicamente um anagrama sem "
            "custar O(K log K) de ordenação?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n"
            "        groups = collections.defaultdict(list)\n"
            "\n"
            "        for s in strs:\n"
            "            count = [0] * 26  # Frequência de cada letra (a-z)\n"
            "            for c in s:\n"
            "                count[ord(c) - ord(\"a\")] += 1\n"
            "\n"
            "            groups[tuple(count)].append(s)  # Tupla é hashable -> vira chave\n"
            "\n"
            "        return list(groups.values())"
        ),
        "reasoning_script": (
            "\"Para agrupar os anagramas eficientemente, preciso de uma Hash Table onde a "
            "chave seja a assinatura comum do anagrama e o valor seja a lista de strings "
            "correspondentes. Em Python, não podemos usar listas mutáveis como chaves de "
            "dicionário porque elas não são 'hashable'. Portanto, tenho duas opções de "
            "chave: ordenar os caracteres da string (o que custa O(K log K) por palavra) "
            "ou criar uma tupla de frequência de 26 posições. Vou optar pela tupla de "
            "frequências, pois garante uma operação linear O(K) sem depender de "
            "ordenação pesada.\""
        ),
        "explanation": (
            "Para cada string, calculamos um vetor de 26 posições com a contagem de cada "
            "letra e convertemos em `tuple` (que é hashable). Strings com a mesma "
            "assinatura de frequência são anagramas e caem na mesma chave do "
            "`defaultdict`."
        ),
        "why_concept": (
            "Usar a tupla de frequências evita o custo de ordenação O(K log K) por string, "
            "reduzindo para O(K), além de resolver o problema de 'hashability' de chaves "
            "mutáveis."
        ),
        "big_o": "O(N × K) tempo, onde N é o número de strings e K o comprimento médio; O(N × K) espaço.",
    },
    {
        "id": "scenario_longest_consecutive_sequence",
        "title": "Busca de Sequências Contínuas em O(N) (Longest Consecutive Sequence)",
        "pillar": "🔑 Hash Tables & Arrays",
        "context": (
            "Encontrar a maior sequência numérica consecutiva em um array desordenado "
            "sem poder ordenar previamente via O(N log N)."
        ),
        "clarifying_questions": [
            "O array pode conter elementos duplicados ou valores negativos?",
            "Existe restrição rígida para que a solução execute estritamente em O(N) de "
            "tempo?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def longestConsecutive(self, nums: List[int]) -> int:\n"
            "        # Converta para um set e identifique apenas os números que são\n"
            "        # 'início' de sequência (ou seja, num - 1 não está no set)\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: como identificar, em O(1), se um número é o "
            "início de uma sequência? Como evitar recontar a mesma sequência várias vezes?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def longestConsecutive(self, nums: List[int]) -> int:\n"
            "        numSet = set(nums)\n"
            "        longest = 0\n"
            "\n"
            "        for n in numSet:\n"
            "            # Só inicia a contagem se 'n' for o começo de uma sequência\n"
            "            if (n - 1) not in numSet:\n"
            "                length = 1\n"
            "                while (n + length) in numSet:\n"
            "                    length += 1\n"
            "                longest = max(longest, length)\n"
            "\n"
            "        return longest"
        ),
        "reasoning_script": (
            "\"Se ordenarmos o array, resolveríamos em O(N log N), mas o problema exige "
            "O(N). Para atingir essa eficiência, vou primeiro converter o array em um Hash "
            "Set para eliminar duplicados e permitir buscas em O(1). O pulo do gato aqui "
            "para evitar loops redundantes é verificar, para cada número, se o seu "
            "antecessor (num - 1) existe no conjunto. Se existir, este número não é o "
            "início de uma sequência, então eu o ignoro. Só começo a contar quando "
            "encontro um número que é genuinamente o início. Isso garante que cada "
            "sequência seja percorrida apenas uma vez, mantendo O(N).\""
        ),
        "explanation": (
            "Ao só iniciar a contagem em números sem antecessor no set, cada sequência é "
            "percorrida exatamente uma vez no total (mesmo que o loop externo passe por "
            "todos os números), mantendo a complexidade amortizada em O(N)."
        ),
        "why_concept": (
            "O Hash Set permite checar a existência do antecessor em O(1), eliminando a "
            "necessidade de ordenação e evitando contagens redundantes de sequências já "
            "visitadas."
        ),
        "big_o": "O(N) tempo (amortizado), O(N) espaço para o set.",
    },
    {
        "id": "scenario_linked_list_cycle",
        "title": "Manipulação de Ponteiros e Detecção de Ciclos (Linked List Cycle)",
        "pillar": "🔗 Linked Lists",
        "context": (
            "Identificar se uma lista encadeada possui um loop interno sem corromper a "
            "estrutura e sem gastar memória excessiva."
        ),
        "clarifying_questions": [
            "Podemos modificar os nós da lista encadeada durante a verificação, ou a "
            "estrutura deve permanecer imutável?",
            "Qual é o comportamento esperado se a lista estiver vazia?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def hasCycle(self, head: Optional[ListNode]) -> bool:\n"
            "        # Implemente o algoritmo de Floyd (dois ponteiros: slow e fast)\n"
            "        # para detectar ciclo em O(1) de espaço\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: como dois ponteiros com velocidades "
            "diferentes podem se encontrar se (e somente se) houver um ciclo?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def hasCycle(self, head: Optional[ListNode]) -> bool:\n"
            "        slow, fast = head, head\n"
            "\n"
            "        while fast and fast.next:\n"
            "            slow = slow.next            # Avança 1 passo\n"
            "            fast = fast.next.next        # Avança 2 passos\n"
            "            if slow == fast:\n"
            "                return True  # Os ponteiros se encontraram -> há ciclo\n"
            "\n"
            "        return False  # 'fast' chegou ao final -> não há ciclo"
        ),
        "reasoning_script": (
            "\"Uma abordagem simples seria usar um Hash Set para armazenar os nós "
            "visitados, mas isso consumiria O(N) de espaço adicional. Para otimizar o "
            "espaço para O(1), vou aplicar o algoritmo dos dois ponteiros de Floyd, "
            "conhecido como 'Tortoise and Hare'. Inicializarei um ponteiro slow que avança "
            "1 passo por vez e um ponteiro fast que avança 2 passos por vez. Se houver um "
            "ciclo, em algum momento o ponteiro rápido alcançará o lento dentro do loop. "
            "Se o ponteiro rápido chegar a null, a lista termina e não há ciclos. Essa "
            "abordagem nos dá tempo O(N) com espaço constante O(1).\""
        ),
        "explanation": (
            "`slow` avança um nó por vez e `fast` avança dois. Se existir um ciclo, "
            "`fast` eventualmente 'dá a volta' dentro do loop e encontra `slow`. Se não "
            "houver ciclo, `fast` chega a `None` antes de qualquer encontro."
        ),
        "why_concept": (
            "O algoritmo de Floyd resolve o problema com espaço O(1), eliminando a "
            "necessidade de um Hash Set O(N) para rastrear nós visitados."
        ),
        "big_o": "O(N) tempo, O(1) espaço.",
    },
    {
        "id": "scenario_valid_parentheses_interview",
        "title": "Validação de Sinais Aninhados com Pilhas (Valid Parentheses)",
        "pillar": "📚 Stacks",
        "context": (
            "Validar a correta abertura e fechamento de chaves, colchetes e parênteses "
            "em uma string."
        ),
        "clarifying_questions": [
            "A string de entrada pode conter caracteres além dos delimitadores (como "
            "letras ou espaços) que devam ser ignorados?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def isValid(self, s: str) -> bool:\n"
            "        # Utilize uma pilha (stack) e um dicionário de mapeamento\n"
            "        # de fechamento -> abertura\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense em voz alta como se estivesse explicando ao "
            "entrevistador: por que uma Pilha (LIFO) resolve naturalmente esse problema?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def isValid(self, s: str) -> bool:\n"
            "        stack = []\n"
            "        closeToOpen = { \")\" : \"(\", \"]\" : \"[\", \"}\" : \"{\" }\n"
            "\n"
            "        for c in s:\n"
            "            if c in closeToOpen:\n"
            "                if stack and stack[-1] == closeToOpen[c]:\n"
            "                    stack.pop()\n"
            "                else:\n"
            "                    return False\n"
            "            else:\n"
            "                stack.append(c)\n"
            "\n"
            "        return True if not stack else False"
        ),
        "reasoning_script": (
            "\"Como estamos lidando com estruturas aninhadas onde o elemento aberto mais "
            "recentemente deve ser o primeiro a ser fechado, o padrão ideal é o LIFO (Last "
            "In, First Out), ou seja, uma Pilha. Vou iterar pela string: quando encontrar "
            "um caractere de abertura, faço um append na pilha. Quando encontrar um "
            "caractere de fechamento, verifico se a pilha não está vazia e se o elemento "
            "no topo corresponde ao par correto mapeado em um dicionário. Se corresponder, "
            "dou um pop. Se não corresponder ou se a pilha estiver vazia ao tentar fechar, "
            "a string é inválida. No final, garanto que a pilha esteja totalmente vazia "
            "para retornar true.\""
        ),
        "explanation": (
            "A pilha guarda os caracteres de abertura pendentes. Cada fechamento deve "
            "corresponder exatamente ao topo da pilha; qualquer divergência ou tentativa "
            "de fechar com a pilha vazia invalida a string."
        ),
        "why_concept": (
            "O comportamento LIFO da Pilha espelha exatamente a regra de aninhamento: o "
            "último elemento aberto deve ser o primeiro a ser fechado."
        ),
        "big_o": "O(N) tempo, O(N) espaço no pior caso.",
    },
    {
        "id": "scenario_max_depth_binary_tree",
        "title": "Recursão vs. Iteração em Árvores (Maximum Depth of Binary Tree)",
        "pillar": "🌳 Árvores / BST",
        "context": "Calcular a profundidade máxima (altura) de uma árvore binária.",
        "clarifying_questions": [
            "A árvore pode ser desbalanceada a ponto de causar estouro de pilha (stack "
            "overflow) na recursão devido à profundidade excessiva?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def maxDepth(self, root: Optional[TreeNode]) -> int:\n"
            "        # Implemente via DFS recursiva (caso base + 1 + max(esquerda, direita))\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: qual é o caso base da recursão? E como você "
            "resolveria o mesmo problema de forma iterativa (BFS) caso a árvore seja "
            "muito profunda?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def maxDepth(self, root: Optional[TreeNode]) -> int:\n"
            "        # Versão recursiva (DFS)\n"
            "        if not root:\n"
            "            return 0  # Caso base: árvore vazia tem profundidade 0\n"
            "        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))\n"
            "\n"
            "    def maxDepthIterativo(self, root: Optional[TreeNode]) -> int:\n"
            "        # Alternativa iterativa (BFS) para evitar estouro de pilha\n"
            "        if not root:\n"
            "            return 0\n"
            "\n"
            "        level, queue = 0, collections.deque([root])\n"
            "        while queue:\n"
            "            for _ in range(len(queue)):\n"
            "                node = queue.popleft()\n"
            "                if node.left:\n"
            "                    queue.append(node.left)\n"
            "                if node.right:\n"
            "                    queue.append(node.right)\n"
            "            level += 1  # Incrementa ao final de cada camada percorrida\n"
            "\n"
            "        return level"
        ),
        "reasoning_script": (
            "\"Para calcular a profundidade máxima, a solução mais limpa e elegante é usar "
            "DFS recursiva: o caso base retorna 0 se o nó for nulo, e o passo recursivo "
            "retorna 1 + max(maxDepth(esquerda), maxDepth(direita)). No entanto, em "
            "ambientes de produção com árvores extremamente profundas e desbalanceadas, a "
            "recursão pode estourar a call stack. Por isso, também posso resolver de "
            "forma iterativa usando uma Fila com Busca em Largura (BFS), incrementando um "
            "contador de níveis a cada camada percorrida. Ambas têm complexidade de O(N), "
            "visitando cada nó uma vez.\""
        ),
        "explanation": (
            "A versão recursiva soma 1 (o nó atual) à maior profundidade entre as "
            "subárvores esquerda e direita. A versão iterativa usa BFS nível a nível, "
            "incrementando o contador `level` a cada camada completa processada."
        ),
        "why_concept": (
            "A recursão é mais simples de escrever, mas a BFS iterativa evita o risco de "
            "`RecursionError` em árvores muito profundas e desbalanceadas — um trade-off "
            "importante de mencionar em entrevista."
        ),
        "big_o": "O(N) tempo em ambas as versões; espaço O(H) na recursiva (altura) e O(N) no pior caso na BFS (largura máxima).",
    },
    {
        "id": "scenario_valid_bst",
        "title": "Validação de Hierarquias Rígidas em Árvores (Valid Binary Search Tree)",
        "pillar": "🌳 Árvores / BST",
        "context": (
            "Garantir que uma árvore binária respeite rigorosamente as regras de uma "
            "BST (tudo à esquerda menor que a raiz, tudo à direita maior)."
        ),
        "clarifying_questions": [
            "Os valores dos nós podem conter números duplicados ou limites extremos "
            "como float('-inf')?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def isValidBST(self, root: Optional[TreeNode]) -> bool:\n"
            "        # Propague um intervalo (low, high) de limites válidos\n"
            "        # para cada nó descendente durante a DFS\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: por que checar apenas os filhos diretos de "
            "cada nó não é suficiente? Como propagar limites válidos ao longo da recursão?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def isValidBST(self, root: Optional[TreeNode]) -> bool:\n"
            "        def valid(node, low, high):\n"
            "            if not node:\n"
            "                return True  # Árvore vazia é válida por definição\n"
            "\n"
            "            if not (low < node.val < high):\n"
            "                return False  # Violou o intervalo permitido\n"
            "\n"
            "            # Ao ir para a esquerda, 'high' vira o valor do nó atual\n"
            "            # Ao ir para a direita, 'low' vira o valor do nó atual\n"
            "            return valid(node.left, low, node.val) and valid(node.right, node.val, high)\n"
            "\n"
            "        return valid(root, float(\"-inf\"), float(\"inf\"))"
        ),
        "reasoning_script": (
            "\"Um erro comum é checar apenas os filhos diretos de cada nó. Isso falharia "
            "se um nó na subárvore esquerda violasse a raiz principal mais acima. Para "
            "evitar isso, não basta checar os filhos imediatos; precisamos propagar um "
            "intervalo de limites válidos (min e max) para cada descendente. Ao ir para a "
            "esquerda, o limite superior passa a ser o valor do nó atual. Ao ir para a "
            "direita, o limite inferior passa a ser o valor do nó atual. Usando essa DFS "
            "com validação de limites estritos, garantimos a integridade da BST em O(N) "
            "de tempo.\""
        ),
        "explanation": (
            "A função `valid` recebe o intervalo `(low, high)` permitido para o valor do "
            "nó atual. A cada chamada recursiva, esse intervalo é restringido conforme "
            "descemos para a esquerda ou direita, garantindo que a regra da BST valha "
            "para toda a árvore, não só localmente."
        ),
        "why_concept": (
            "Propagar limites (`low`, `high`) via DFS captura violações 'distantes' na "
            "árvore que uma checagem apenas local (comparando só com o pai imediato) não "
            "detectaria."
        ),
        "big_o": "O(N) tempo (visita cada nó uma vez), O(H) espaço de recursão (H = altura da árvore).",
    },
    {
        "id": "scenario_number_of_islands_interview",
        "title": "Travessia de Matrizes e Prevenção de Loops em Grafos (Number of Islands)",
        "pillar": "🌐 Grafos / DFS",
        "context": "Contar componentes conexos em uma matriz 2D (grade de terra e água).",
        "clarifying_questions": [
            "As diagonais contam como conexões ou apenas movimentos horizontais e "
            "verticais?",
            "Podemos modificar os dados da matriz original ('in-place') para marcar as "
            "células visitadas e economizar memória?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def numIslands(self, grid: List[List[str]]) -> int:\n"
            "        # Varra a matriz e, ao achar terra não visitada, acione uma DFS/BFS\n"
            "        # que 'afunda' toda a ilha conectada\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: como você evitaria processar a mesma célula "
            "mais de uma vez (e cair em loop)? Por que a marcação in-place resolve isso?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def numIslands(self, grid: List[List[str]]) -> int:\n"
            "        if not grid:\n"
            "            return 0\n"
            "\n"
            "        ROWS, COLS = len(grid), len(grid[0])\n"
            "        islands = 0\n"
            "\n"
            "        def dfs(r, c):\n"
            "            if (r < 0 or c < 0 or r >= ROWS or c >= COLS\n"
            "                    or grid[r][c] == \"0\"):\n"
            "                return\n"
            "\n"
            "            grid[r][c] = \"0\"  # Marca como visitada ('afunda' a terra)\n"
            "            dfs(r + 1, c)\n"
            "            dfs(r - 1, c)\n"
            "            dfs(r, c + 1)\n"
            "            dfs(r, c - 1)\n"
            "\n"
            "        for r in range(ROWS):\n"
            "            for c in range(COLS):\n"
            "                if grid[r][c] == \"1\":\n"
            "                    islands += 1  # Encontrou o início de uma nova ilha\n"
            "                    dfs(r, c)     # Afunda toda a ilha conectada\n"
            "\n"
            "        return islands"
        ),
        "reasoning_script": (
            "\"Assumindo que apenas movimentos horizontais e verticais formam conexões, "
            "vou varrer a matriz com dois loops. Quando encontrar um '1' (terra), sei que "
            "achei o início de uma nova ilha, então incremento meu contador. A partir "
            "daí, aciono uma DFS (ou BFS) para explorar todas as células vizinhas "
            "conectadas e as 'afundo' marcando-as como '0'. Essa marcação in-place é "
            "essencial para evitar loops infinitos, pois impede que a mesma célula seja "
            "processada múltiplas vezes. A complexidade de tempo será O(M × N), onde M é "
            "o número de linhas e N o de colunas.\""
        ),
        "explanation": (
            "Cada célula de terra ainda não visitada dispara uma DFS que marca toda a "
            "ilha conectada como água, impedindo que ela seja contada novamente nas "
            "próximas iterações do loop principal."
        ),
        "why_concept": (
            "A marcação in-place elimina a necessidade de uma estrutura `visited` "
            "separada, economizando espaço extra, e garante terminação da DFS (sem "
            "ciclos) ao 'consumir' a terra já explorada."
        ),
        "big_o": "O(M × N) tempo, O(M × N) espaço no pior caso (pilha de recursão em uma ilha que cobre toda a grade).",
    },
    {
        "id": "scenario_rotting_oranges",
        "title": "Simulação de Propagação de Estado com BFS (Rotting Oranges)",
        "pillar": "🌐 Grafos / BFS",
        "context": (
            "Calcular o tempo mínimo necessário para que uma condição se propague por "
            "vizinhança em uma grade (ex.: laranjas podres contaminando as frescas)."
        ),
        "clarifying_questions": [
            "O que deve ser retornado se for fisicamente impossível propagar a condição "
            "para todas as unidades?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def orangesRotting(self, grid: List[List[int]]) -> int:\n"
            "        # Inicialize a BFS com TODAS as laranjas podres de uma vez\n"
            "        # (multi-source BFS) e avance nível a nível (minuto a minuto)\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: por que a BFS deve começar de todas as "
            "fontes 'podres' ao mesmo tempo, em vez de uma só? Como você mediria o tempo "
            "decorrido?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def orangesRotting(self, grid: List[List[int]]) -> int:\n"
            "        ROWS, COLS = len(grid), len(grid[0])\n"
            "        queue = collections.deque()\n"
            "        fresh = 0\n"
            "\n"
            "        # Coleta todas as laranjas podres (multi-source) e conta as frescas\n"
            "        for r in range(ROWS):\n"
            "            for c in range(COLS):\n"
            "                if grid[r][c] == 2:\n"
            "                    queue.append((r, c))\n"
            "                elif grid[r][c] == 1:\n"
            "                    fresh += 1\n"
            "\n"
            "        minutes = 0\n"
            "        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]\n"
            "\n"
            "        while queue and fresh > 0:\n"
            "            for _ in range(len(queue)):  # Processa uma camada (1 minuto)\n"
            "                r, c = queue.popleft()\n"
            "                for dr, dc in directions:\n"
            "                    nr, nc = r + dr, c + dc\n"
            "                    if (0 <= nr < ROWS and 0 <= nc < COLS\n"
            "                            and grid[nr][nc] == 1):\n"
            "                        grid[nr][nc] = 2  # Apodrece a laranja vizinha\n"
            "                        fresh -= 1\n"
            "                        queue.append((nr, nc))\n"
            "            minutes += 1\n"
            "\n"
            "        return minutes if fresh == 0 else -1"
        ),
        "reasoning_script": (
            "\"Como o problema pede o menor tempo para propagar a condição camada por "
            "camada (minuto a minuto), a abordagem correta é a Busca em Largura (BFS). Um "
            "detalhe crítico aqui é que a BFS não deve começar de uma única fonte, mas "
            "sim ser inicializada coletando todas as laranjas podres simultaneamente e "
            "jogando-as na fila. Enquanto isso, conto quantas laranjas frescas existem. A "
            "cada nível da BFS que processamos, decremento o contador de frutas frescas e "
            "avanço o relógio em 1 minuto. Se ao final a contagem de frutas frescas for "
            "zero, retorno o tempo acumulado; caso contrário, retorno -1.\""
        ),
        "explanation": (
            "A fila começa com todas as laranjas já podres (multi-source BFS). Cada "
            "iteração do `while` processa uma camada inteira (um minuto), apodrecendo "
            "todas as laranjas frescas adjacentes às já podres naquele instante."
        ),
        "why_concept": (
            "Multi-source BFS propaga todas as fontes 'em paralelo', garantindo que o "
            "número de camadas processadas corresponda exatamente ao tempo mínimo "
            "necessário — uma única BFS normal (fonte única) não modelaria a propagação "
            "simultânea corretamente."
        ),
        "big_o": "O(M × N) tempo (cada célula processada uma vez), O(M × N) espaço para a fila no pior caso.",
    },
    {
        "id": "scenario_find_min_rotated_sorted_array",
        "title": "Busca Binária em Estruturas Modificadas (Find Minimum in Rotated Sorted Array)",
        "pillar": "🔍 Busca Binária",
        "context": (
            "Encontrar o menor elemento em um array que estava ordenado mas sofreu "
            "rotações desconhecidas."
        ),
        "clarifying_questions": [
            "Todos os elementos do array são únicos ou existem números duplicados?",
        ],
        "skeleton_code": (
            "class Solution:\n"
            "    def findMin(self, nums: List[int]) -> int:\n"
            "        # Implemente uma busca binária modificada: a cada passo, identifique\n"
            "        # qual metade está ordenada e descarte a outra\n"
            "        pass"
        ),
        "reasoning_prompt": (
            "Antes de ver a solução, pense: como comparar `nums[mid]` com `nums[right]` "
            "ajuda a decidir qual metade do array está 'perfeitamente' ordenada?"
        ),
        "solution_code": (
            "class Solution:\n"
            "    def findMin(self, nums: List[int]) -> int:\n"
            "        left, right = 0, len(nums) - 1\n"
            "\n"
            "        while left < right:\n"
            "            mid = (left + right) // 2\n"
            "\n"
            "            if nums[mid] < nums[right]:\n"
            "                # Metade direita está ordenada -> mínimo está em [left, mid]\n"
            "                right = mid\n"
            "            else:\n"
            "                # Ponto de inflexão está na metade esquerda -> mínimo em [mid+1, right]\n"
            "                left = mid + 1\n"
            "\n"
            "        return nums[left]"
        ),
        "reasoning_script": (
            "\"Embora uma busca linear encontrasse o mínimo em O(N), a restrição pede "
            "eficiência em O(log N), o que me direciona imediatamente para a Busca "
            "Binária modificada. Em um array ordenado e rotacionado, se cortarmos o "
            "array ao meio, uma das metades estará sempre perfeitamente ordenada, "
            "enquanto a outra conterá o ponto de inflexão da rotação. Vou comparar o "
            "elemento do meio (mid) com o elemento da extrema direita (right). Se "
            "nums[mid] < nums[right], sei que a metade direita está ordenada e o mínimo "
            "está na metade esquerda (incluindo o mid). Caso contrário, o mínimo está na "
            "metade direita. Dessa forma, descarto metade dos dados a cada iteração, "
            "alcançando a complexidade O(log N).\""
        ),
        "explanation": (
            "Se `nums[mid] < nums[right]`, o mínimo não pode estar à direita de `mid` "
            "(essa metade já está ordenada e crescente), então movemos `right = mid`. "
            "Caso contrário, o ponto de rotação está entre `mid` e `right`, então "
            "movemos `left = mid + 1`. O loop termina quando `left == right`, apontando "
            "para o menor elemento."
        ),
        "why_concept": (
            "Mesmo com a rotação 'quebrando' a ordenação global, uma das metades "
            "permanece localmente ordenada em qualquer divisão ao meio — essa invariante "
            "é o que permite aplicar busca binária e manter O(log N)."
        ),
        "big_o": "O(log N) tempo, O(1) espaço.",
    },
]

