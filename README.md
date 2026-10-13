# 🧠 Amazon SDE-II Interview Quiz

Aplicativo web interativo, feito com [Streamlit](https://streamlit.io/), para praticar
entrevistas técnicas de **Software Development Engineer II (SDE-II)**, com foco nos
tópicos de algoritmos e estruturas de dados mais cobrados em processos seletivos
como o da Amazon.

🔗 **App publicado:** [share.streamlit.io](https://share.streamlit.io/) (deploy via Streamlit Community Cloud)

## 💡 Sobre o projeto

O quiz cobre os 5 pilares mais recorrentes em entrevistas técnicas:

1. 📊 **Arrays, Hash Tables e Hashing**
2. 🔗 **Linked Lists, Stacks e Queues**
3. 🌳 **Trees e Binary Search Trees (BST)**
4. 🕸️ **Grafos, BFS e DFS**
5. 🔍 **Busca Binária e Ordenação**

Cada módulo contém perguntas de dois tipos:

- **Conceituais (`mcq`)**: múltipla escolha sobre teoria, complexidade e trade-offs.
- **Depuração de código (`code`)**: snippets de código para analisar, identificar
  complexidade (Big O) e entender o comportamento do algoritmo.

Ao responder, o app mostra se a resposta está correta, exibe uma explicação técnica
detalhada e a notação Big O relacionada, ajudando a fixar o raciocínio por trás da
solução — e não apenas decorar a resposta certa.

## 🚀 Como executar localmente

### Pré-requisitos

- [Python 3.9+](https://www.python.org/downloads/) instalado
- `pip` disponível no terminal

### Passo a passo

1. Clone o repositório:

   ```bash
   git clone https://github.com/marisouzaent/amazon-sde2-interview-quiz.git
   cd amazon-sde2-interview-quiz
   ```

2. (Recomendado) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv

   # Windows (PowerShell)
   venv\Scripts\Activate.ps1

   # macOS/Linux
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Rode o app:

   ```bash
   streamlit run app.py
   ```

5. O Streamlit abrirá automaticamente no navegador em `http://localhost:8501`.
   Caso não abra, acesse esse endereço manualmente.

## 📁 Estrutura do projeto

```
amazon-sde2-interview-quiz/
├── app.py               # Interface e lógica do quiz (Streamlit)
├── questions_data.py    # Banco de perguntas, organizado por módulo
├── requirements.txt     # Dependências do projeto
└── README.md
```

## 🛠️ Tecnologias

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

## 🤝 Contribuindo

Sugestões de novas perguntas, correções ou melhorias são bem-vindas! Sinta-se
à vontade para abrir uma *issue* ou enviar um *pull request*.
