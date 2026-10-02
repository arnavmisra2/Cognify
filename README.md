

# 📚 Cognify — AI-Powered Study Assistant

Cognify is an AI-powered study assistant designed to help students understand, revise, and learn from their study materials more efficiently.

Upload a PDF and interact with it using natural language. Cognify uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the uploaded document and generate context-aware answers.

---

## ✨ Features

### 📄 PDF-Based Learning
Upload your study material in PDF format and let Cognify process and index the document.

### 💬 Ask Anything
Ask questions about your uploaded document and receive answers based on its content.

### 📖 Explain
Get difficult concepts explained in a simple, student-friendly way.

### 📝 Summarize
Generate concise summaries of relevant sections of your study material.

### 🎯 Exam Mode
Get answers structured specifically for exam preparation, including important points and key concepts.

### ❓ Quiz Me
Generate practice questions from your uploaded study material.

### 🧠 Flashcards
Create revision-friendly flashcards from the document.

### 🔍 Key Concepts
Identify important concepts and topics that deserve attention while studying.

### 📑 Page-Aware Answers
Cognify keeps track of document pages while processing the PDF, allowing retrieved context to include page references.

### 🎨 Study-Focused Interface
The application uses a clean study-desk interface designed around reading, understanding, and revision rather than a generic chatbot experience.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| LangChain | RAG and LLM orchestration |
| LangChain Community | Document loading and integrations |
| LangChain Groq | Groq LLM integration |
| ChromaDB | Vector database |
| Hugging Face | Text embeddings |
| Sentence Transformers | Document embeddings |
| PyPDF | PDF processing |
| Groq | Large Language Model inference |

---

## 🧠 How Cognify Works

Cognify follows a Retrieval-Augmented Generation (RAG) pipeline.

```text
              ┌─────────────────┐
              │    Upload PDF   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Extract Text   │
              │    from PDF     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Split into      │
              │     Chunks      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Generate        │
              │ Embeddings      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   ChromaDB      │
              │ Vector Store    │
              └────────┬────────┘
                       │
                 User Question
                       │
                       ▼
              ┌─────────────────┐
              │ Retrieve        │
              │ Relevant Chunks │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Groq LLM      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Context-Aware   │
              │     Answer      │
              └─────────────────┘
📂 Project Structure
Smart-Study-Buddy/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
│
├── .venv/
│
└── README.md
Important Files

app.py

Contains the main Streamlit application, PDF processing pipeline, RAG implementation, study modes, UI, and chat functionality.

requirements.txt

Contains the Python dependencies required to run the application.

.env

Stores environment variables such as the Groq API key.

⚠️ Never commit .env to GitHub.

.gitignore

Prevents sensitive files and local environments such as .env and .venv/ from being committed.

⚙️ Installation
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/Smart-Study-Buddy.git

Navigate into the project:

cd Smart-Study-Buddy
2. Create a Virtual Environment

On Windows:

python -m venv .venv

Activate it:

.\.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

If you want to use the Streamlit PDF viewer:

pip install "streamlit[pdf]"
🔑 API Configuration

Cognify uses Groq for LLM inference.

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key

Your project should look like:

Smart-Study-Buddy/
│
├── app.py
├── requirements.txt
├── .env
└── .gitignore
Security

Never share your API key publicly.

Make sure .gitignore contains:

.env
.venv/
venv/
__pycache__/
*.pyc
.chromadb/
chroma_db/
▶️ Running the Application

From the project directory:

.\.venv\Scripts\python.exe -m streamlit run app.py

Alternatively, if your virtual environment is activated:

streamlit run app.py

The application will open in your browser.

📖 How to Use
Step 1 — Upload a PDF

Open Cognify and upload your study material from the sidebar.

Step 2 — Wait for Processing

Cognify extracts the PDF text, divides it into chunks, generates embeddings, and stores them in ChromaDB.

Step 3 — Select a Study Mode

Choose the type of assistance you need:

Ask Anything
     ↓
Explain
     ↓
Summarize
     ↓
Exam Mode
     ↓
Quiz Me
     ↓
Flashcards
     ↓
Key Concepts
Step 4 — Ask Your Question

Use the chat interface to interact with your study material.

Cognify retrieves relevant information from your uploaded document before generating the response.

🧩 RAG Pipeline

Cognify uses the following RAG workflow:

1. Document Loading

PDF documents are loaded using PyPDFLoader.

2. Text Splitting

Large documents are divided into smaller chunks using:

RecursiveCharacterTextSplitter

The application uses overlapping chunks to preserve contextual information.

3. Embeddings

The application generates vector representations using:

all-MiniLM-L6-v2

through Hugging Face/Sentence Transformers.

4. Vector Storage

The generated embeddings are stored in:

ChromaDB
5. Retrieval

When the user asks a question, Cognify retrieves relevant document chunks.

6. Generation

The retrieved context is passed to the Groq-powered language model to generate the response.

🎓 Study Modes
Ask Anything

General question-answering using the uploaded document as the primary source.

Explain

Designed to simplify difficult concepts for students.

Summarize

Produces concise summaries of relevant material.

Exam Mode

Structures responses for exam preparation and emphasizes important points.

Quiz Me

Generates practice questions from the uploaded document.

Flashcards

Creates short question-and-answer cards for revision.

Key Concepts

Identifies important concepts from the document.

🔐 Security

Cognify uses environment variables for API credentials.

Never hard-code your API key:

GROQ_API_KEY = "your-key"

Instead, use:

GROQ_API_KEY=your-key

and load it through environment variables.

The following files should remain private:

.env
.venv/
🚀 Future Improvements

Possible future improvements include:

📚 Multiple-document knowledge base
🔎 Advanced document search
📌 Better source/page citations
🗂️ Document library
📝 Personal notes
📊 Learning analytics
🎯 Exam preparation dashboard
🧠 Spaced-repetition flashcards
📈 Study progress tracking
🔐 User authentication
☁️ Cloud deployment
🎤 Voice-based interaction
🐛 Troubleshooting
ModuleNotFoundError

Make sure the project virtual environment is being used:

.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"

It should point to:

Smart-Study-Buddy\.venv\Scripts\python.exe

Then install dependencies:

.\.venv\Scripts\python.exe -m pip install -r requirements.txt
PDF Viewer Error

If Streamlit reports that the PDF viewer component is missing:

.\.venv\Scripts\python.exe -m pip install --upgrade "streamlit[pdf]"
Groq API Error

Check that .env exists in the project root:

Smart-Study-Buddy/
├── app.py
├── .env
└── requirements.txt

and contains:

GROQ_API_KEY=your_actual_key
📌 Project Status

Cognify is an actively developed AI-powered study assistant focused on PDF-based learning, retrieval-augmented question answering, and interactive study tools.

👨‍💻 Author

Arnav Misra

B.Tech — Computer Science / Data Science

⭐ Support

If you find Cognify useful, consider giving the repository a ⭐ on GitHub.

📄 License

This project is intended for educational and development purposes.


### Save it

Create a file named:

```text
README.md

in:

C:\Users\dell\OneDrive\Desktop\pdfreader\Smart-Study-Buddy

Then push it:

git add README.md
git commit -m "Add Cognify README"
git push origin main

One thing I would change before you publish it: replace YOUR_USERNAME/Smart-Study-Buddy with your actual GitHub repository URL.

make the readme more ellaborate 

Done — I made the README much more detailed and GitHub-ready. It now includes:

📚 Detailed project overview
🧠 Complete RAG architecture and workflow
🎓 All 7 Cognify study modes
🛠️ Full technology stack
📂 Project structure
⚙️ Installation instructions
🔐 .env and API-key security
▶️ Running instructions for Windows/Linux/macOS
📖 Detailed usage workflow
🗃️ ChromaDB/vector-store explanation
🧩 Mode-aware prompting
🐛 Troubleshooting
🔄 Development/Git workflow
🚀 Future roadmap
📊 Project highlights
🤝 Contribution guide
👨‍💻 Author section
📌 Current implemented/planned features

Download the expanded README.md

Put this file in:

Smart-Study-Buddy/
├── app.py
├── requirements.txt
├── README.md  ← replace your current one
├── .gitignore
└── .env

Then push it with:

git add README.md
git commit -m "Expand Cognify documentation"
git push origin main
README.md
Document

Library
/
README.md
📚 Cognify — AI-Powered Study Assistant

Learn from your documents. Understand difficult concepts. Revise smarter. Prepare better.

Cognify is an AI-powered study assistant designed to turn static PDF study material into an interactive learning workspace. Students can upload notes, textbooks, presentations, or other PDF material and interact with the content using natural language.

Cognify uses a Retrieval-Augmented Generation (RAG) pipeline to extract document content, split it into meaningful chunks, generate semantic embeddings, store those embeddings in ChromaDB, retrieve relevant context for each question, and generate a contextual response through a Groq-hosted language model.

✨ Features
📄 PDF-Based Learning

Upload PDF study material and let Cognify process it for semantic search and question answering.

💬 Ask Anything

Ask natural-language questions about the uploaded document. Cognify retrieves relevant document context before generating the answer.

📖 Explain

Understand difficult concepts through clear, student-friendly explanations, examples, comparisons, and step-by-step descriptions.

📝 Summarize

Generate concise summaries of relevant document material for quick revision.

🎯 Exam Mode

Prepare exam-oriented answers with definitions, important points, comparisons, advantages, disadvantages, examples, and structured explanations.

❓ Quiz Me

Generate practice questions from the uploaded study material to support active recall and self-testing.

🧠 Flashcards

Turn important information into question-and-answer flashcards for quick revision.

🔍 Key Concepts

Identify important concepts and topics from the study material so students can prioritize revision.

📑 Page-Aware Context

PDF page metadata is retained during document processing, allowing retrieved context to include page references such as [Page 4].

🎨 Study-Focused UI

Cognify is designed as a study workspace rather than a generic chatbot, with study modes, a central document area, and an AI study companion.

🧠 RAG Architecture
                    ┌─────────────────┐
                    │    Upload PDF   │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │  Extract Text   │
                    │    PyPDFLoader  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │  Split Content  │
                    │   into Chunks   │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │    Generate     │
                    │   Embeddings    │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │    ChromaDB     │
                    │  Vector Store   │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Student Question│
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Retrieve Top    │
                    │ Relevant Chunks │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │   LangChain     │
                    │    RAG Chain    │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │     Groq LLM    │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Final Context-  │
                    │ Aware Response  │
                    └─────────────────┘
How it works
Upload: The student uploads a PDF through Streamlit.
Extraction: PyPDFLoader extracts the document text and metadata.
Chunking: RecursiveCharacterTextSplitter divides the document into smaller overlapping chunks.
Embedding: all-MiniLM-L6-v2 converts chunks into semantic vectors through Hugging Face/Sentence Transformers.
Storage: ChromaDB stores the vectors for similarity search.
Retrieval: A student's question is used to retrieve the most relevant document chunks.
Prompting: Retrieved context, the selected study mode, and the student's question are combined into a prompt.
Generation: The Groq-hosted language model generates the response.

The application currently uses a chunking configuration based on:

RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

and retrieves multiple relevant chunks for the response.

🎓 Study Modes
Mode	Purpose
💬 Ask Anything	General document-grounded question answering
📖 Explain	Simplify and explain difficult concepts
📝 Summarize	Produce concise summaries
🎯 Exam Mode	Prepare structured exam-oriented answers
❓ Quiz Me	Generate practice questions
🧠 Flashcards	Create revision flashcards
🔍 Key Concepts	Identify important topics and concepts
Example prompts
What is a recurrent neural network?

Explain LSTM in simple words.

Compare GRU and LSTM.

Explain this topic for 8 marks.

Summarize this chapter.

Quiz me on the most important concepts.

Create flashcards from this topic.
🖥️ Application Layout

Cognify follows a three-area study workspace:

┌────────────────┬──────────────────────────┬─────────────────┐
│ STUDY MODES    │ CURRENT DOCUMENT         │ AI COMPANION    │
│                │                          │                 │
│ Ask Anything   │                          │ Study Chat      │
│ Explain        │       PDF Viewer         │ Answers         │
│ Summarize      │                          │ Explanations    │
│ Exam Mode      │                          │ Revision        │
│ Quiz Me        │                          │                 │
│ Flashcards     │                          │                 │
│ Key Concepts   │                          │                 │
└────────────────┴──────────────────────────┴─────────────────┘

The design follows a simple learning cycle:

Select → Understand → Remember

🛠️ Technology Stack
Technology	Purpose
Python	Core application logic
Streamlit	Web interface
LangChain	RAG and LLM orchestration
LangChain Community	Document/vector-store integrations
LangChain Groq	Groq model integration
ChromaDB	Vector database
Hugging Face	Embedding model ecosystem
Sentence Transformers	Semantic embeddings
PyPDF	PDF extraction
Groq	LLM inference
python-dotenv	Environment configuration
Current LLM configuration

The application is configured to use:

openai/gpt-oss-120b

through the LangChain Groq integration. Model availability can change, so the configured model should be verified before deployment.

📂 Project Structure
Smart-Study-Buddy/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git exclusions
├── .env                   # Private API configuration (do not commit)
│
└── .venv/                 # Local Python virtual environment
app.py

Contains the main application, including:

Streamlit interface
Session-state management
PDF upload and processing
Text splitting
Hugging Face embeddings
ChromaDB vector storage
LangChain RAG chain
Groq integration
Study modes
Chat functionality
PDF viewer
requirements.txt

Contains the packages required to install and run Cognify.

.env

Stores sensitive environment variables such as the Groq API key.

.gitignore

Prevents sensitive and local development files from being committed.

⚙️ Installation
Prerequisites

Before installing Cognify, make sure you have:

Python installed
Git installed
A Groq API key
Internet access for package installation and API calls
A terminal such as PowerShell, Command Prompt, or Bash
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/Smart-Study-Buddy.git
cd Smart-Study-Buddy

Replace YOUR_USERNAME with the GitHub account that owns the repository.

2. Create a Virtual Environment
Windows
python -m venv .venv
.\.venv\Scripts\activate
Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

Using a dedicated environment prevents project dependencies from conflicting with packages installed in another Python or Anaconda environment.

3. Install Dependencies
pip install -r requirements.txt

For the Streamlit PDF viewer, install the PDF extra if it is not already included:

pip install "streamlit[pdf]"
🔐 Environment Variables

Create .env in the project root:

GROQ_API_KEY=your_actual_groq_api_key

The project loads the key with python-dotenv.

Example:

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
Security

Never commit .env to GitHub.

Recommended .gitignore entries:

.venv/
venv/
.env
__pycache__/
*.pyc
.chromadb/
chroma_db/

If an API key is accidentally exposed, revoke/rotate it immediately.

▶️ Running the Application

If the virtual environment is activated:

streamlit run app.py

On Windows, the project environment can also be used explicitly:

.\.venv\Scripts\python.exe -m streamlit run app.py

This explicit command is useful when multiple Python installations are present.

📖 How to Use Cognify
Step 1 — Launch

Start the Streamlit application.

Step 2 — Upload

Upload a PDF from the document uploader.

Step 3 — Process

Cognify extracts the PDF content, splits it into chunks, generates embeddings, and indexes the content in ChromaDB.

Step 4 — Select a Mode

Choose a study mode based on your goal.

Step 5 — Ask

Ask questions in natural language from the AI study companion.

Step 6 — Revise

Use Summary, Quiz, Flashcards, and Key Concepts modes to reinforce learning.

🧪 Example Learning Workflow

Suppose a student uploads:

DeepLearning_Unit-IV.pdf

A possible study session is:

Upload PDF
    ↓
Key Concepts
    ↓
Explain difficult topics
    ↓
Summarize the unit
    ↓
Prepare 8-mark answers
    ↓
Quiz Me
    ↓
Flashcards
    ↓
Final revision

This supports a progression from understanding → revision → testing → active recall.

🔄 Application State

Cognify uses Streamlit session state to maintain information across Streamlit reruns.

Important state values include:

pdf_processed
pdf_name
pdf_bytes
vectorstore
chat_history
study_mode
chat_open
collection_name

When a new PDF is selected, document-related state is reset before the new document is indexed.

🗃️ Vector Store Lifecycle

A simplified document lifecycle is:

PDF selected
    ↓
Extract pages
    ↓
Create chunks
    ↓
Generate embeddings
    ↓
Create vector collection
    ↓
Store in ChromaDB
    ↓
Retrieve relevant chunks
    ↓
Generate answer

A unique collection name can be used for each processing session so that different uploaded documents do not unintentionally share the same collection.

🧩 Mode-Aware Prompting

The retrieval mechanism can remain consistent while the response instruction changes according to the selected study mode.

For example:

Ask Anything  → General document-grounded answer
Explain       → Educational explanation
Summarize     → Concise summary
Exam Mode     → Exam-oriented response
Quiz Me       → Practice questions
Flashcards    → Question/answer cards
Key Concepts  → Important topics

This allows one RAG workflow to support multiple learning activities.

🔒 Security Best Practices
Never hard-code API keys.
Never commit .env.
Keep .venv/ outside Git tracking.
Do not share credentials in screenshots or logs.
Rotate exposed API keys immediately.
Use environment variables for secrets.
Review git status before pushing changes.

Before committing, verify that sensitive files are absent:

git status

You should not see .env or .venv/ in the staged changes.

🐛 Troubleshooting
ModuleNotFoundError

If you see errors such as:

ModuleNotFoundError: No module named 'langchain_community'

make sure the project virtual environment is being used:

.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"

It should point to something similar to:

Smart-Study-Buddy\.venv\Scripts\python.exe

Then install the requirements into that exact environment:

.\.venv\Scripts\python.exe -m pip install -r requirements.txt
PDF Viewer Error

If Streamlit reports that the PDF viewer component is missing:

.\.venv\Scripts\python.exe -m pip install --upgrade "streamlit[pdf]"
Groq API Error

Check that .env is located next to app.py:

Smart-Study-Buddy/
├── app.py
├── .env
└── requirements.txt

Then confirm the variable is named exactly:

GROQ_API_KEY=your_actual_groq_api_key
Model Not Found / Unavailable

If Groq returns an error that a model is unavailable, verify the currently supported model name in your Groq account/API and update the model_name setting in app.py.

Dependency Conflicts

Use a clean virtual environment when resolving major dependency problems:

python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

Avoid installing a large number of unrelated packages manually because transitive dependencies may conflict.

🚀 Future Roadmap

Cognify is designed to grow into a broader personal learning platform.

📚 Document Library

Allow students to organize multiple documents by subject, semester, unit, or course.

📝 Personal Notes

Save useful AI explanations, summaries, and important sections as personal notes.

📊 Learning Analytics

Track:

Questions asked
Topics studied
Quiz performance
Revision activity
Flashcards reviewed
🎯 Exam Dashboard

Provide:

Subject tracking
Unit progress
Important topics
Revision status
Practice questions
Exam preparation progress
🔎 Enhanced Source Citations

Improve source references with document page numbers and retrieved sections so students can quickly verify an answer against the original material.

🧠 Spaced Repetition

Schedule flashcards using spaced-repetition techniques for repeated review.

👤 User Accounts

Potential support for:

Authentication
Personal study history
Saved notes
Document collections
Progress tracking
☁️ Deployment

Prepare the application for production deployment with secure environment-variable management, dependency verification, model configuration, and application monitoring.

🎯 Project Objectives
Reduce Study Friction

Make it easier to move from a long PDF to a useful explanation or revision resource.

Encourage Active Learning

Quiz and flashcard workflows encourage recall instead of passive rereading.

Simplify Complex Concepts

Explain mode is intended to make difficult material more approachable.

Support Examination Preparation

Exam Mode helps transform source material into structured academic answers.

Keep Responses Contextual

The RAG pipeline retrieves content from the student's uploaded document before generating a response.

📊 Project Highlights
Category	Implementation
Interface	Streamlit
Document format	PDF
Document loader	PyPDFLoader
Text splitter	RecursiveCharacterTextSplitter
Embedding model	all-MiniLM-L6-v2
Vector database	ChromaDB
Retrieval	LangChain Retriever
LLM provider	Groq
LLM integration	LangChain Groq
Configuration	.env
Application state	Streamlit Session State
🧪 Development Workflow

A typical development cycle is:

Modify Code
    ↓
Run Streamlit
    ↓
Test PDF Upload
    ↓
Test Retrieval
    ↓
Test Study Modes
    ↓
Check Errors
    ↓
Review git status
    ↓
Commit
    ↓
Push to GitHub

Recommended Git commands:

git status
git add .
git commit -m "Update Cognify"
git push origin main

Always check git status before committing to make sure secrets such as .env are not included.

🤝 Contributing

Contributions and suggestions are welcome.

Typical workflow:

git clone <repository-url>
cd Smart-Study-Buddy
git checkout -b feature/your-feature

Make your changes, then:

git add .
git commit -m "Add your feature"
git push origin feature/your-feature

Open a pull request after pushing the branch.

👨‍💻 Author
Arnav Misra

B.Tech — Computer Science / Data Science

Cognify is an AI and Data Science project exploring:

Retrieval-Augmented Generation
Large Language Models
Natural Language Processing
Semantic search
Vector databases
Document intelligence
AI-powered educational applications
📜 License

This project is intended primarily for educational and development purposes.

If a specific open-source license is added to the repository, replace this section with the corresponding license terms.

📌 Project Status

Status: Active Development

Implemented

PDF upload

PDF text extraction

Text chunking

Hugging Face embeddings

ChromaDB vector storage

RAG-based question answering

Groq LLM integration

Ask Anything mode

Explain mode

Summarize mode

Exam Mode

Quiz Mode

Flashcard Mode

Key Concepts mode

PDF viewer

Study-focused UI

Planned

Document library

Personal notes

Learning analytics

Improved source citations

Exam preparation dashboard

Spaced-repetition system

User accounts

Expanded deployment support

⭐ Cognify

Read less. Understand more. Remember better.

Cognify brings document understanding, AI assistance, revision, and active learning into one study-focused workspace.