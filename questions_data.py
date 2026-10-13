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
