# -*- coding: utf-8 -*-
"""
Amazon SDE-II Interview Prep - Quiz Técnico
=============================================
Aplicativo Streamlit interativo para prática de entrevistas técnicas de
Software Development Engineer II (SDE-II), cobrindo os 5 pilares mais
cobrados: Arrays/Hashing, Linked Lists/Stacks/Queues, Trees/BST,
Grafos/BFS/DFS e Busca Binária/Ordenação.

Para executar localmente:
    pip install -r requirements.txt
    streamlit run app.py
"""

import streamlit as st

from questions_data import MODULES

# ----------------------------------------------------------------------------
# Configuração da página
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Amazon SDE-II Quiz Prep",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# CSS customizado — visual moderno inspirado na paleta Amazon
# ----------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
    :root {
        --amazon-orange: #FF9900;
        --amazon-navy: #232F3E;
    }

    .main-header {
        background: linear-gradient(90deg, var(--amazon-navy) 0%, #37475A 100%);
        padding: 1.75rem 2rem;
        border-radius: 14px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    }
    .main-header h1 {
        color: #FFFFFF;
        margin: 0;
        font-size: 2.1rem;
    }
    .main-header p {
        color: #D5DBDB;
        margin: 0.4rem 0 0 0;
        font-size: 1.02rem;
    }

    .module-desc {
        background-color: rgba(255, 153, 0, 0.08);
        border-left: 4px solid var(--amazon-orange);
        padding: 0.9rem 1.1rem;
        border-radius: 8px;
        margin-bottom: 1.4rem;
        font-size: 0.97rem;
    }

    .question-card {
        background-color: rgba(128, 128, 128, 0.06);
        border: 1px solid rgba(128, 128, 128, 0.18);
        border-radius: 12px;
        padding: 1.3rem 1.4rem 0.9rem 1.4rem;
        margin-bottom: 1.4rem;
    }

    .big-o-note {
        background-color: rgba(35, 47, 62, 0.06);
        border-radius: 8px;
        padding: 0.6rem 0.9rem;
        font-size: 0.88rem;
        margin-top: 0.5rem;
        border: 1px dashed rgba(255, 153, 0, 0.6);
    }

    div.stButton > button {
        background-color: var(--amazon-orange);
        color: #111;
        font-weight: 600;
        border: none;
        border-radius: 8px;
    }
    div.stButton > button:hover {
        background-color: #e68a00;
        color: #fff;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128,128,128,0.2);
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Estado da sessão
# ----------------------------------------------------------------------------
def init_session_state() -> None:
    if "results" not in st.session_state:
        # Mapeia question_id -> bool (True = acertou, False = errou)
        st.session_state.results = {}
    if "current_module" not in st.session_state:
        st.session_state.current_module = "home"


def total_questions() -> int:
    return sum(len(m["questions"]) for m in MODULES.values())


def reset_progress() -> None:
    st.session_state.results = {}
    # Limpa também os widgets de radio para desmarcar seleções antigas
    for key in list(st.session_state.keys()):
        if key.startswith("radio_"):
            del st.session_state[key]


# ----------------------------------------------------------------------------
# Sidebar — navegação e placar
# ----------------------------------------------------------------------------
def render_sidebar() -> str:
    st.sidebar.markdown("## 🧭 Navegação")

    nav_options = {"🏠 Início": "home"}
    for key, mod in MODULES.items():
        nav_options[f'{mod["icon"]} {mod["title"].split(" ", 1)[1]}'] = key

    labels = list(nav_options.keys())
    default_label = labels[0]
    for label, key in nav_options.items():
        if key == st.session_state.current_module:
            default_label = label
            break

    choice_label = st.sidebar.radio(
        "Selecione um módulo de estudo:",
        labels,
        index=labels.index(default_label),
        key="sidebar_nav",
    )
    selected_key = nav_options[choice_label]
    st.session_state.current_module = selected_key

    st.sidebar.markdown("---")
    st.sidebar.markdown("## 📈 Progresso Geral")

    total = total_questions()
    answered = len(st.session_state.results)
    correct = sum(1 for v in st.session_state.results.values() if v)

    st.sidebar.progress(answered / total if total else 0)
    st.sidebar.caption(f"{answered}/{total} perguntas respondidas")

    col_a, col_b = st.sidebar.columns(2)
    col_a.metric("✅ Acertos", correct)
    col_b.metric("❌ Erros", answered - correct)

    if answered > 0:
        taxa = 100 * correct / answered
        st.sidebar.caption(f"Taxa de acerto: **{taxa:.0f}%**")

    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 Reiniciar Progresso", use_container_width=True):
        reset_progress()
        st.rerun()

    return selected_key


# ----------------------------------------------------------------------------
# Renderização de uma pergunta
# ----------------------------------------------------------------------------
def render_question(question: dict, order: int) -> None:
    qid = question["id"]

    with st.container():
        st.markdown('<div class="question-card">', unsafe_allow_html=True)

        badge = "💻 Depuração de Código" if question["type"] == "code" else "🧩 Conceitual"
        st.markdown(f"**Questão {order}** &nbsp;·&nbsp; _{badge}_")
        st.markdown(question["question"])

        if question.get("code"):
            st.code(question["code"], language="python")

        radio_key = f"radio_{qid}"
        selected = st.radio(
            "Escolha uma alternativa:",
            question["options"],
            index=None,
            key=radio_key,
            label_visibility="collapsed",
        )

        col1, col2 = st.columns([1, 4])
        with col1:
            verify_clicked = st.button("Verificar Resposta", key=f"check_{qid}")

        if verify_clicked:
            if selected is None:
                st.warning("⚠️ Selecione uma alternativa antes de verificar.")
            else:
                selected_index = question["options"].index(selected)
                is_correct = selected_index == question["answer"]
                st.session_state.results[qid] = is_correct

        # Exibe feedback persistente se a questão já foi verificada
        if qid in st.session_state.results:
            is_correct = st.session_state.results[qid]
            correct_option = question["options"][question["answer"]]

            if is_correct:
                st.success("✅ **Correto!**")
            else:
                st.error(f"❌ **Incorreto.** A resposta certa é: _{correct_option}_")

            st.info(f"**Por quê:** {question['explanation']}")
            st.markdown(
                f'<div class="big-o-note">📐 <b>Complexidade (Big O):</b> {question["big_o"]}</div>',
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# Página de um módulo
# ----------------------------------------------------------------------------
def render_module(module_key: str) -> None:
    module = MODULES[module_key]

    st.markdown(
        f"""
        <div class="main-header">
            <h1>{module['title']}</h1>
            <p>Módulo de prática — responda e receba feedback técnico imediato</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f'<div class="module-desc">🎯 {module["description"]}</div>', unsafe_allow_html=True)

    for idx, question in enumerate(module["questions"], start=1):
        render_question(question, idx)

    # Placar do módulo
    module_ids = [q["id"] for q in module["questions"]]
    answered_in_module = [qid for qid in module_ids if qid in st.session_state.results]
    correct_in_module = sum(1 for qid in answered_in_module if st.session_state.results[qid])

    st.markdown("---")
    st.markdown(
        f"### 🏆 Pontuação neste módulo: {correct_in_module}/{len(module_ids)} "
        f"({len(answered_in_module)} respondidas de {len(module_ids)})"
    )


# ----------------------------------------------------------------------------
# Página inicial
# ----------------------------------------------------------------------------
def render_home() -> None:
    st.markdown(
        """
        <div class="main-header">
            <h1>🧠 Amazon SDE-II Interview Prep</h1>
            <p>Plataforma pessoal de quiz técnico para preparação de entrevistas de
            Software Development Engineer II</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        Bem-vindo(a) ao seu espaço de treino técnico! Este quiz cobre os **5 pilares**
        mais recorrentes em entrevistas de algoritmos e estruturas de dados nível
        SDE-II, com foco especial em:

        - Reconhecer e **otimizar complexidade** (ex.: O(N²) → O(N));
        - Identificar **armadilhas comuns de código** (estouro de índice, ponteiros
          mutáveis mal gerenciados, loops infinitos);
        - Justificar cada resposta com **Big O notation**.

        Use o menu lateral para escolher um módulo e comece a praticar. Seu progresso
        é mantido durante a sessão atual.
        """
    )

    st.markdown("### 📚 Módulos disponíveis")
    cols = st.columns(len(MODULES))
    for col, (key, module) in zip(cols, MODULES.items()):
        with col:
            st.markdown(
                f"""
                <div class="question-card" style="text-align:center; min-height: 190px;">
                    <h2 style="margin-bottom:0.2rem;">{module['icon']}</h2>
                    <b>{module['title'].split(' ', 1)[1]}</b>
                    <p style="font-size:0.82rem; margin-top:0.5rem;">
                        {len(module['questions'])} questões
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    total = total_questions()
    answered = len(st.session_state.results)
    correct = sum(1 for v in st.session_state.results.values() if v)

    st.markdown("### 📊 Seu desempenho até agora")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total de perguntas", total)
    c2.metric("Respondidas", answered)
    c3.metric("Acertos", correct, delta=f"{100 * correct / answered:.0f}% de acerto" if answered else None)


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main() -> None:
    init_session_state()
    selected_module = render_sidebar()

    if selected_module == "home":
        render_home()
    else:
        render_module(selected_module)


if __name__ == "__main__":
    main()
