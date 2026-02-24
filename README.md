# 🦜🔗 LangChain Course — CampusX YouTube Channel Practice

> A comprehensive collection of practice scripts, notebooks, and examples from the [CampusX](https://www.youtube.com/@campusx-official) LangChain course. Each section covers a specific concept with standalone, runnable scripts organized by topic.

---

## 📋 Table of Contents

- [⚙️ Requirements](#️-requirements)
- [🚀 Setup](#-setup)
- [🗂️ Project Structure](#️-project-structure)
  - [01-Fundamentals](#-01-fundamentals)
  - [02-RAG](#-02-rag)
  - [03-Agents](#-03-agents)
  - [🗃️ Root-level Files](#️-root-level-files)
- [▶️ Running Examples](#️-running-examples)
- [📝 Notes](#-notes)
- [📄 License](#-license)

---

## ⚙️ Requirements

- 🐍 Python 3.10+
- 🌐 A virtual environment (`venv`, `conda`, `uv`, etc.)
- 🔑 API keys set via environment variables (see your provider's docs)

---

## 🚀 Setup

1. Clone the repo and create/activate a virtual environment.
2. Install dependencies from `pyproject.toml`:

```bash
pip install .
```

Or sync from the lockfile using `uv`:

```bash
uv sync
```

---

## 🗂️ Project Structure

```
langchain-course-campusx/
├── 01-Fundamentals/
│   ├── 01-models-define/
│   ├── 02-similarity-score/
│   ├── 03-prompts/
│   ├── 04-chatbot/
│   ├── 05-messages/
│   ├── 06-output-parsers/
│   ├── 07-chains/
│   └── 08-Runnables/
├── 02-RAG/
│   ├── 09-documents-loader/
│   ├── 10-text-splitters/
│   ├── 11-vector-stores/
│   ├── 12-retrievers/
│   └── 13-rag-system/
├── 03-Agents/
│   ├── 14-built-in-tools/
│   ├── 15-custom-tools/
│   ├── 16-tools-calling/
│   └── 17-Simple-Agent/
├── main.py
├── main.ipynb
├── pyproject.toml
└── ...
```

---

## 🧱 01-Fundamentals

> Core LangChain concepts and building blocks — start here!

### 🤖 01-models-define

Covers how to define and interact with different LLM/embedding models.

| File | Description |
|------|-------------|
| `01_chat_model.py` | Basic chat model usage with LangChain's `ChatOpenAI` or similar |
| `02_embeddings_model_local.py` | Load and use a locally hosted embeddings model |
| `03_embeddings_model_inference_api.py` | Use HuggingFace Inference API to generate embeddings |

---

### 📐 02-similarity-score

Learn how to measure semantic similarity between documents.

| File | Description |
|------|-------------|
| `04_document_similarity_score.py` | Compute cosine/dot-product similarity scores between documents using embeddings |

---

### 📝 03-prompts

Explore static and dynamic prompt creation with LangChain prompt templates.

| File | Description |
|------|-------------|
| `05_static_prompts_ui.py` | Build a simple UI to test static prompt templates |
| `06_dynamic_prompts.py` | Dynamically construct prompts at runtime using variables |
| `07_prompt_template_generator.py` | Generate reusable prompt templates programmatically |

---

### 💬 04-chatbot

Build your first chatbot with LangChain.

| File | Description |
|------|-------------|
| `08_simple_chatbot.py` | A minimal chatbot that takes user input and returns model responses |

---

### ✉️ 05-messages

Understand LangChain's message types and how to manage conversation history.

| File | Description |
|------|-------------|
| `09_messages.py` | Explore `HumanMessage`, `AIMessage`, `SystemMessage` objects |
| `10_chatbot_with_messages.py` | Build a chatbot that maintains a list of messages as history |
| `11_chat_prompt_template.py` | Use `ChatPromptTemplate` to structure multi-turn prompts |
| `12_message_place_holder.py` | Inject dynamic message history using `MessagesPlaceholder` |

---

### 🔧 06-output-parsers

Parse and structure model outputs into usable Python objects.

| File | Description |
|------|-------------|
| `13_typed_dictionary.py` | Define output schemas using Python's `TypedDict` |
| `14_structured_output_typed_dict.py` | Force models to return structured output matching a `TypedDict` |
| `15_using_ollama_model.py` | Use a locally running Ollama model as the LLM backend |
| `16_pydantic.py` | Define output schemas using Pydantic `BaseModel` |
| `17_structured_output_pydantic.py` | Use `.with_structured_output()` with a Pydantic schema |
| `18_simple_output.py` | Minimal example of raw model output parsing |
| `19_str_output_parser.py` | Parse model output as a plain string using `StrOutputParser` |
| `20_json_output_parser.py` | Parse model output as JSON using `JsonOutputParser` |
| `21_pydantic_output_parser.py` | Full Pydantic output parser with schema validation |

---

### ⛓️ 07-chains

Compose multiple steps together using LangChain chains.

| File | Description |
|------|-------------|
| `22_simple_chain.py` | Connect a prompt template and model into a basic chain using `|` operator |
| `23_sequential_chains.py` | Run chains one after another, passing output from one to the next |
| `24_parallel_chains.py` | Execute multiple chains simultaneously and combine their results |
| `25_conditional_chains.py` | Route to different chains based on input conditions |

---

### 🔀 08-Runnables

Deep dive into the LangChain Expression Language (LCEL) runnable primitives.

| File | Description |
|------|-------------|
| `26_runnables_sequence.py` | Chain runnables in a sequence using `RunnableSequence` |
| `27_runnables_parallel.py` | Run runnables in parallel using `RunnableParallel` |
| `28_runnables_passthrough.py` | Pass input through unchanged using `RunnablePassthrough` |
| `29_runnables_lambda.py` | Wrap arbitrary Python functions as runnables using `RunnableLambda` |
| `30_runnables_branch.py` | Conditional branching with `RunnableBranch` |
| `31_runnables_branch_lcel.py` | Implement branching logic using LCEL syntax |
| `32_runnables_parallel_lcel.py` | Parallel execution expressed in LCEL syntax |

---

## 📡 02-RAG

> Retrieval-Augmented Generation — ground your LLM in real documents!

### 📂 09-documents-loader

Load documents from various sources into LangChain `Document` objects.

| File | Description |
|------|-------------|
| `33_text_file_loader.py` | Load plain `.txt` files using `TextLoader` |
| `34_pdf_loader.py` | Load PDF files using `PyPDFLoader` |
| `35_directory_loader.py` | Bulk-load all documents from a directory |
| `36_web_based_loader.py` | Scrape and load content from web URLs |
| `37_blog_question_answer.py` | End-to-end Q&A pipeline over a blog post loaded from the web |
| `38_csv_loader.py` | Load tabular data from CSV files into documents |

---

### ✂️ 10-text-splitters

Split large documents into smaller chunks for effective retrieval.

| File | Description |
|------|-------------|
| `39_length_based.py` | Split text by character count using `CharacterTextSplitter` |
| `40_length_based_doc_loader.py` | Combine document loading and length-based splitting in one step |
| `41_text_structure_based.py` | Split text respecting natural structure (paragraphs, sentences) with `RecursiveCharacterTextSplitter` |
| `42_text_structure_based_on_code.py` | Language-aware splitting for source code (Python, JS, etc.) |
| `43_semantic_text_splitters.py` | Semantically group sentences using embedding similarity before splitting |

---

### 🗄️ 11-vector-stores

Store and query document embeddings with vector databases.

| File | Description |
|------|-------------|
| `44_chroma.py` | Create, persist, and query a Chroma vector store |
| `44_chroma.ipynb` | Interactive Jupyter notebook walkthrough of Chroma |

---

### 🔍 12-retrievers

Retrieve relevant document chunks given a query.

| File | Description |
|------|-------------|
| `45_wikipedia_retriever.py` | Retrieve live Wikipedia articles as context using `WikipediaRetriever` |
| `46_vector_store_retriever.py` | Convert a vector store into a retriever for similarity search |
| `47_mmr.py` | Use Maximum Marginal Relevance (MMR) for diverse, non-redundant retrieval |
| `48_multiquery_retriever.py` | Generate multiple query variants to improve recall |
| `49_contextual_compression_retriever.py` | Compress retrieved chunks to keep only query-relevant content |

---

### 🏗️ 13-rag-system

A complete, modular end-to-end RAG pipeline built step by step.

| File | Description |
|------|-------------|
| `youtube_transcript_loader_50.py` | Load and parse YouTube video transcripts as documents |
| `text_splitter_51.py` | Split transcript documents into manageable chunks |
| `embeddings_vector_store_52.py` | Embed chunks and store them in a Chroma vector store |
| `retriever_53.py` | Configure the retriever on top of the vector store |
| `prompt_context_54.py` | Build the RAG prompt that injects retrieved context |
| `model_55.py` | Configure the LLM used for answer generation |
| `final_chain_56.py` | Assemble all components into the final LCEL RAG chain |
| `main_57.ipynb` | Jupyter notebook demonstrating the full RAG pipeline interactively |
| `main_58.py` | Python script version of the complete RAG pipeline |
| `README.md` | Documentation specific to this RAG system module |

---

## 🤖 03-Agents

> Build autonomous agents that reason, use tools, and take actions!

### 🛠️ 14-built-in-tools

Use LangChain's pre-built tools to give agents real-world capabilities.

| File | Description |
|------|-------------|
| `59_duckduckgo_search.py` | Give the agent web search capability using DuckDuckGo |
| `60_shell_tool.py` | Allow the agent to execute shell commands on the local machine |

---

### 🔩 15-custom-tools

Create your own tools for agents to use.

| File | Description |
|------|-------------|
| `61_simple_multiply_tool.py` | Define a minimal custom tool that multiplies two numbers |
| `62_structured_tool.py` | Build a structured tool with typed input schema using `StructuredTool` |
| `63_using@tool.py` | Create tools using the convenient `@tool` decorator |
| `64_base_tool_class.py` | Build a tool by subclassing LangChain's `BaseTool` for full control |
| `65_toolkit.py` | Group multiple related tools into a `Toolkit` for organised agent use |

---

### 📞 16-tools-calling

Wire tools into the LLM call cycle and handle tool execution.

| File | Description |
|------|-------------|
| `66_tools_binding.py` | Bind tools to a model so it knows what tools are available |
| `67_tools_calling.py` | Invoke the model and observe it generating tool-call requests |
| `68_tools_execution.py` | Execute the tool calls requested by the model and return results |
| `69_main.ipynb` | Interactive notebook tying tools binding, calling, and execution together |
| `currency_conversion_70.py` | Currency conversion tool used as a practical example |
| `conversion_factor_tool_71.py` | Tool that looks up unit conversion factors |
| `convert_72.py` | Tool that performs the actual unit/currency conversion calculation |

---

### 🧠 17-Simple-Agent

Put it all together — a fully autonomous ReAct-style agent.

| File | Description |
|------|-------------|
| `73_agent.py` | Build and run a simple ReAct agent that reasons, selects tools, and acts autonomously |

---

## 🗃️ Root-level Files

| File | Description |
|------|-------------|
| `main.py` | Pulls a ReAct prompt from LangSmith using the LangSmith Python SDK |
| `main.ipynb` | Root-level Jupyter notebook for quick experiments |
| `chat_history.txt` | Persisted chat conversation history from chatbot examples |
| `drug200.csv` | Sample drug dataset used in CSV loader / data experiments |
| `file.csv` | Generic CSV sample file used in document loader examples |
| `file.pdf` | Sample PDF used in PDF loader examples |
| `file.txt` | Sample plain-text file used in text loader examples |
| `prompt_template.json` | Saved prompt template configuration in JSON format |
| `pyproject.toml` | Project metadata, dependencies, and build configuration |
| `uv.lock` | Locked dependency versions for reproducible installs with `uv` |
| `.env` | Local environment variables (API keys — **never commit this!**) |
| `.gitignore` | Files and folders excluded from version control |
| `.python-version` | Specifies the Python version for this project |

---

## ▶️ Running Examples

Run any script directly:

```bash
python 01-Fundamentals/01-models-define/01_chat_model.py
```

Run a Jupyter notebook:

```bash
jupyter notebook 02-RAG/13-rag-system/main_57.ipynb
```

---

## 📝 Notes

- 🔒 **Keep your API keys out of source control** — use `.env` and `.gitignore`.
- 📈 Scripts are **incremental** — later examples build on earlier concepts.
- 🧩 Each file is designed to be **runnable independently** within its section.
- 💡 Review inline comments in each script for detailed concept explanations.

---

## 📄 License

For learning and personal practice only.
