import os
import tempfile
import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage


# ============================================================
# CONFIG
# ============================================================

load_dotenv()

st.set_page_config(
    page_title="Cognify",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

/* =========================================================
   GLOBAL
========================================================= */

.stApp {
    background: #f5f3ee;
    color: #20201e;
    font-family: "Inter", sans-serif;
}

.main .block-container {
    max-width: 1500px;
    padding-top: 0.8rem;
    padding-bottom: 2rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

h1, h2, h3 {
    font-family: Georgia, "Times New Roman", serif;
    color: #20201e;
}

p, span, label {
    color: #4b4a46;
}


/* =========================================================
   SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {
    background: #9A8068 !important;
    border-right: 1px solid #806750 !important;
}

section[data-testid="stSidebar"] > div:first-child {
    background: #9A8068 !important;
    padding-top: 1.5rem;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #FFF8EE !important;
}

section[data-testid="stSidebar"] h1 {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1.8rem;
    font-weight: 600;
}


/* =========================================================
   FILE UPLOADER
========================================================= */

section[data-testid="stSidebar"] [data-testid="stFileUploader"] {
    background: #F8F3EB !important;
    border: 1px solid rgba(255, 255, 255, 0.75) !important;
    border-radius: 8px !important;
    padding: 0.45rem !important;
}

section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
    background: #EFE5D8 !important;
    border: 1px dashed #B29A82 !important;
    border-radius: 6px !important;
}

section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] span,
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] small {
    color: #4F3A2B !important;
}

section[data-testid="stSidebar"] [data-testid="stFileUploader"] button {
    background: #6B503B !important;
    color: #FFF8EE !important;
    border: 1px solid #4F3A2B !important;
    border-radius: 6px !important;
}

section[data-testid="stSidebar"] [data-testid="stFileUploader"] button:hover {
    background: #4F3A2B !important;
}


/* =========================================================
   GENERAL BUTTONS
========================================================= */

.stButton > button {
    background: #faf9f5 !important;
    border: 1px solid #d2cec3 !important;
    color: #292824 !important;
    border-radius: 7px !important;
    min-height: 0 !important;
    padding: 0.55rem 0.8rem !important;
    box-shadow: none !important;
    transition: all 0.15s ease;
}

.stButton > button:hover {
    background: #efede7 !important;
    border-color: #77736b !important;
}


/* =========================================================
   MAIN HEADER
========================================================= */

.cognify-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.1rem 0 0.35rem 0;
}

.cognify-header h1 {
    margin: 0;
    font-size: 2rem;
}

.eyebrow {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    color: #88837a;
    margin-bottom: 0.15rem;
}

.header-status {
    font-size: 0.72rem;
    color: #88837a;
}

.desk-divider {
    height: 1px;
    background: #d8d4ca;
    margin-bottom: 0.9rem;
}


/* =========================================================
   LEFT COGNIFY PANEL
========================================================= */

.ai-panel {
    padding: 0.2rem 0.15rem;
}

.ai-eyebrow {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    color: #99938a;
}

.ai-title {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1.35rem;
    margin-top: 0.35rem;
    color: #292621;
    line-height: 1.15;
}

.ai-description {
    font-size: 0.76rem;
    line-height: 1.5;
    color: #777168;
    margin-top: 0.45rem;
}

.ai-divider {
    height: 1px;
    background: #ddd8ce;
    margin: 1.2rem 0;
}

.ai-section-title {
    font-size: 0.61rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #99938a;
    margin-bottom: 0.65rem;
}


/* =========================================================
   DOCUMENT AREA
========================================================= */

.document-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-bottom: 0.65rem;
}

.document-eyebrow {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #99938a;
}

.document-title {
    font-size: 1rem;
    font-weight: 600;
    margin-top: 0.15rem;
}

.document-meta {
    font-size: 0.68rem;
    color: #99938a;
    letter-spacing: 0.08em;
}

.empty-document {
    min-height: 650px;
    border: 1px dashed #d4d0c6;
    border-radius: 6px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: #f8f6f1;
}

.empty-document-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.empty-document-title {
    font-family: Georgia, serif;
    font-size: 1.35rem;
    color: #302d29;
    margin-bottom: 0.4rem;
}

.empty-document-text {
    font-size: 0.78rem;
    color: #88837a;
    max-width: 280px;
    line-height: 1.6;
}


/* =========================================================
   KEYED PANELS
========================================================= */

.st-key-study_controls {
    padding: 0.2rem 0.1rem;
}

.st-key-study_controls [data-testid="stButton"] {
    margin-bottom: 0.35rem;
}

.st-key-empty_document {
    min-height: 650px;
    border: 1px dashed #d4d0c6;
    border-radius: 6px;
    background: #f8f6f1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 2rem;
}

.st-key-right_chat_panel {
    background: #18181b;
    color: #f5f3ee;
    border: 1px solid #2a2927;
    border-radius: 7px;
    padding: 0.9rem;
    min-height: 600px;
}

.st-key-right_chat_panel p,
.st-key-right_chat_panel label,
.st-key-right_chat_panel span {
    color: #c9c4bb;
}

.st-key-right_chat_panel h3 {
    color: #f5f3ee !important;
}

.st-key-right_chat_panel [data-testid="stChatMessage"] {
    background: transparent !important;
}

.st-key-right_chat_panel [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p {
    color: #f5f3ee !important;
}

/* =========================================================
   PDF VIEWER
========================================================= */

[data-testid="stPdf"] {
    border: 1px solid #ddd8ce;
    border-radius: 6px;
    overflow: hidden;
}


/* =========================================================
   RIGHT CHAT PANEL
========================================================= */

.chat-panel {
    background: #f8f6f1;
    border: 1px solid #d8d4ca;
    border-radius: 7px;
    padding: 0.9rem;
}

.chat-panel-title {
    font-family: Georgia, serif;
    font-size: 1.15rem;
    color: #292621;
}

.chat-panel-description {
    font-size: 0.74rem;
    color: #777168;
    line-height: 1.45;
    margin-top: 0.35rem;
    margin-bottom: 0.8rem;
}

.chat-empty {
    border: 1px dashed #d5d0c6;
    border-radius: 6px;
    padding: 1.5rem 0.8rem;
    text-align: center;
    color: #88837a;
    font-size: 0.75rem;
    line-height: 1.5;
    margin-top: 0.8rem;
}


/* =========================================================
   CHAT MESSAGES
========================================================= */

.ai-bubble {
    background: #eeece6;
    color: #292824;
    padding: 0.85rem 1rem;
    border-left: 3px solid #77736b;
    border-radius: 0 7px 7px 0;
    margin: 0.6rem 0;
    line-height: 1.55;
    font-size: 0.86rem;
}

.user-bubble {
    background: #292824;
    color: #ffffff !important;
    padding: 0.75rem 0.9rem;
    border-radius: 7px;
    margin: 0.6rem 0 0.6rem auto;
    max-width: 90%;
    line-height: 1.5;
    font-size: 0.84rem;
}

.avatar-ai,
.avatar-user {
    font-size: 0.61rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #88837a;
}

.avatar-user {
    text-align: right;
}


/* =========================================================
   CHAT INPUT
========================================================= */

[data-testid="stChatInput"] {
    border-top: none !important;
    padding-top: 0.5rem !important;
}

[data-testid="stChatInput"] textarea {
    background: #faf9f5 !important;
    color: #24231f !important;
    border: 1px solid #cbc7bd !important;
    border-radius: 7px !important;
}


/* =========================================================
   ALERTS
========================================================= */

[data-testid="stAlert"] {
    border-radius: 7px;
}


/* =========================================================
   HIDE OLD RADIO UI IF ANY
========================================================= */

div[role="radiogroup"] {
    display: none;
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

if "pdf_bytes" not in st.session_state:
    st.session_state.pdf_bytes = None

if "study_mode" not in st.session_state:
    st.session_state.study_mode = "Ask Anything"

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False


# ============================================================
# SIDEBAR — PDF UPLOAD
# ============================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/book.png",
        width=60,
    )

    st.title("Cognify")

    st.markdown("---")

    st.markdown("### Upload Your Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
    )

    # --------------------------------------------------------
    # NEW PDF DETECTED
    # --------------------------------------------------------

    if uploaded_file and uploaded_file.name != st.session_state.pdf_name:

        st.session_state.pdf_processed = False
        st.session_state.vectorstore = None
        st.session_state.chat_history = []
        st.session_state.pdf_name = uploaded_file.name
        st.session_state.pdf_bytes = uploaded_file.getvalue()
        st.session_state.study_mode = "Ask Anything"
        st.session_state.chat_open = False

    # --------------------------------------------------------
    # PDF PROCESSING
    # --------------------------------------------------------

    if (
        uploaded_file
        and not st.session_state.pdf_processed
        and st.session_state.pdf_bytes is not None
    ):

        with st.spinner("Reading and indexing your PDF..."):

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:

                tmp_file.write(st.session_state.pdf_bytes)

                tmp_path = tmp_file.name

            loader = PyPDFLoader(tmp_path)

            documents = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
            )

            chunks = splitter.split_documents(documents)

            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

            st.session_state.vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=embeddings,
                collection_name="cognify_pdf_collection",
            )

            st.session_state.pdf_processed = True

        st.toast(
            f"📄 {st.session_state.pdf_name} loaded successfully!",
            icon="✅",
        )

        st.rerun()

    # --------------------------------------------------------
    # LOADED DOCUMENT STATUS
    # --------------------------------------------------------

    if st.session_state.pdf_processed:

        st.success(f"Loaded: {st.session_state.pdf_name}")

        if st.button(
            "Clear Chat",
            use_container_width=True,
            key="clear_chat_btn",
        ):

            st.session_state.chat_history = []

            st.rerun()

    st.markdown("---")

    st.markdown("### How it works")

    st.markdown(
        """
1. Upload a PDF
2. Choose a study mode
3. Ask Cognify
4. Get answers from your document
"""
    )

    st.markdown("---")

    st.caption("Powered by Groq + LangChain + ChromaDB")


# ============================================================
# MAIN HEADER
# ============================================================

header_left, header_right = st.columns([4, 1])

with header_left:
    st.caption("STUDY DESK")
    st.markdown("## Cognify")

with header_right:
    st.caption("Your personal study workspace")

st.markdown("---")


# ============================================================
# MAIN THREE-COLUMN LAYOUT
# LEFT   = Study controls
# CENTER = PDF document
# RIGHT  = AI companion
# ============================================================

left_col, document_col, right_col = st.columns(
    [1.15, 2.45, 1.4],
    gap="small",
)


# ============================================================
# LEFT — STUDY COMPANION
# ============================================================

with left_col:
    with st.container(key="study_controls"):
        st.caption("COGNIFY")
        st.markdown("### Study companion")
        st.caption("Understand, review, and remember what you're studying.")
        st.markdown("---")
        st.caption("QUICK ACTIONS")

        mode_buttons = [
            ("💬  Ask Anything", "Ask Anything", "cognify_ask_anything"),
            ("📖  Explain", "📖 Explain", "cognify_explain"),
            ("📝  Summarize", "📝 Summarize", "cognify_summarize"),
            ("🎯  Exam Mode", "🎯 Exam Mode", "cognify_exam"),
            ("❓  Quiz Me", "❓ Quiz Me", "cognify_quiz"),
            ("🧠  Flashcards", "🧠 Flashcards", "cognify_flashcards"),
            ("🔍  Key Concepts", "🔍 Key Concepts", "cognify_key_concepts"),
        ]

        for label, mode, key in mode_buttons:
            if st.button(label, key=key, use_container_width=True):
                st.session_state.study_mode = mode
                st.session_state.chat_open = True
                st.rerun()


# ============================================================
# CENTER — DOCUMENT
# ============================================================

with document_col:
    if st.session_state.pdf_processed:
        doc_left, doc_right = st.columns([4, 1])

        with doc_left:
            st.caption("CURRENT DOCUMENT")
            st.markdown(f"**{st.session_state.pdf_name}**")

        with doc_right:
            st.caption("PDF")

        st.pdf(
            st.session_state.pdf_bytes,
            height=720,
        )

    else:
        with st.container(key="empty_document"):
            st.markdown("### 📖")
            st.markdown("## No document selected")
            st.caption(
                "Upload a PDF from the sidebar to begin your study session."
            )


# ============================================================
# RIGHT — AI COMPANION
# ============================================================

with right_col:
    with st.container(key="right_chat_panel"):
        st.caption("COGNIFY")
        st.markdown("### Study companion")
        st.caption("Ask questions and study directly from your document.")
        st.markdown("---")

        if not st.session_state.chat_open:
            st.caption("STUDY CHAT")
            st.info(
                "Choose **Ask Anything** or another study mode from the left "
                "to open your document conversation here."
            )
            question = None

        else:
            clean_mode = (
                st.session_state.study_mode
                .replace("📖 ", "")
                .replace("📝 ", "")
                .replace("🎯 ", "")
                .replace("❓ ", "")
                .replace("🧠 ", "")
                .replace("🔍 ", "")
            )

            st.caption(clean_mode.upper())

            for message in st.session_state.chat_history:
                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.markdown(message.content)
                else:
                    with st.chat_message("assistant"):
                        st.markdown(message.content)

            if st.session_state.study_mode == "Ask Anything":
                placeholder = "Ask something about your PDF..."
            else:
                placeholder = f"Ask Cognify in {clean_mode} mode..."

            question = st.chat_input(
                placeholder,
                key="cognify_document_chat",
            )


# ============================================================
# AI PROMPTS
# ============================================================

mode_prompts = {
    "📖 Explain": (
        "Explain the most important topic in this document "
        "in a clear, student-friendly way. Include definitions, "
        "important details, and examples only when they are "
        "present in the document."
    ),
    "📝 Summarize": (
        "Create a clear summary of this document. Organize "
        "it into headings and bullet points. Include the major "
        "ideas and important details found in the document. "
        "Do not add outside information."
    ),
    "🎯 Exam Mode": (
        "Analyze this document for exam preparation. Identify "
        "the most important topics, definitions, concepts, "
        "formulas, processes, and points that a student should "
        "study. Organize them by topic and use only information "
        "supported by the document."
    ),
    "❓ Quiz Me": (
        "Create a practice quiz from this document. Generate "
        "10 questions covering important material. Prefer "
        "multiple-choice questions with four options and "
        "clearly mark the correct answer after each question. "
        "Use only information from the document."
    ),
    "🧠 Flashcards": (
        "Create 10 useful study flashcards from this document. "
        "Format each as Question and Answer. Focus on important "
        "definitions, concepts, facts, and processes. Use only "
        "information from the document."
    ),
    "🔍 Key Concepts": (
        "Extract the key concepts from this document. For each "
        "concept, give its name and a short, clear explanation "
        "based only on the document. Organize the result in a "
        "readable list."
    ),
}


# ============================================================
# CHAT / RAG PROCESSING
# ============================================================

if st.session_state.pdf_processed and st.session_state.chat_open and question:

    user_request = question

    # --------------------------------------------------------
    # SAVE USER MESSAGE
    # --------------------------------------------------------

    st.session_state.chat_history.append(HumanMessage(content=user_request))

    # --------------------------------------------------------
    # CONVERSATION HISTORY
    # --------------------------------------------------------

    history_text = ""

    for msg in st.session_state.chat_history[:-1]:

        role = "User" if isinstance(msg, HumanMessage) else "Assistant"

        history_text += f"{role}: {msg.content}\n"

    # --------------------------------------------------------
    # LLM
    # --------------------------------------------------------

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="openai/gpt-oss-120b",
        temperature=0.1,
    )

    # --------------------------------------------------------
    # PROMPT
    # --------------------------------------------------------

    prompt = ChatPromptTemplate.from_template(
        """
You are Cognify, a helpful study assistant.

Answer ONLY using the document content provided below.

Rules:

- Use only information supported by the document.
- Never invent information.
- Never use outside knowledge unless the user explicitly asks
  for it.
- If the requested information is not in the document, say:
  "I couldn't find that in the document."
- Make explanations clear for a college student.
- Use headings and bullet points when useful.
- For follow-up questions, use the previous conversation.
- Be accurate and concise.

Previous conversation:

{history}

Document context:

{context}

Current request:

{input}

Answer:
"""
    )

    # --------------------------------------------------------
    # RETRIEVER
    # --------------------------------------------------------

    retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 5})

    def format_docs(docs):

        return "\n\n".join(doc.page_content for doc in docs)

    # --------------------------------------------------------
    # RAG CHAIN
    # --------------------------------------------------------

    rag_chain = (
        {
            "context": retriever | format_docs,
            "input": RunnablePassthrough(),
            "history": lambda _: history_text,
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    # --------------------------------------------------------
    # RUN AI
    # --------------------------------------------------------

    with st.spinner("Cognify is thinking..."):

        full_query = user_request

        if history_text:

            full_query = f"{history_text}\n" f"Follow-up question: {user_request}"

        answer = rag_chain.invoke(full_query)

    # --------------------------------------------------------
    # SAVE AI RESPONSE
    # --------------------------------------------------------

    st.session_state.chat_history.append(AIMessage(content=answer))

    st.rerun()


# ============================================================
# NO PDF MESSAGE
# ============================================================

if not st.session_state.pdf_processed:

    st.info("Upload a PDF from the sidebar to start studying.")
