# LangChain Course from CampusX Youtube Channel Practice

This repository contains comprehensive practice scripts and examples from a LangChain course. Each section covers specific concepts with standalone, runnable scripts organized by topic.

## Requirements

- Python 3.10+ recommended
- A virtual environment (venv, conda, etc.)
- API keys set via environment variables (see your provider's docs)

## Setup

1. Create and activate a virtual environment.
2. Install dependencies from `pyproject.toml`:

```bash
pip install .
```

If you use `uv`, you can sync from the lockfile:

```bash
uv sync
```

## Project Structure

### 01-Fundamentals

Core LangChain concepts and building blocks.

#### 01_models_define
- `01_chat_model.py` - Basic chat model usage
- `02_embeddings_model_local.py` - Local embeddings model
- `03_embeddings_model_inference_api.py` - Inference API embeddings

#### 02_similarity_score
- `04_document_similarity_score.py` - Computing document similarity scores

#### 03_prompts
- `05_static_prompts_ui.py` - Static prompt templates with UI
- `06_dynamic_prompts.py` - Dynamic prompt creation
- `07_prompt_template_generator.py` - Prompt template generation

#### 04_chatbot
- `08_simple_chatbot.py` - Basic chatbot implementation

#### 05_messages
- `09_messages.py` - Working with message objects
- `10_chatbot_with_messages.py` - Chatbot using messages
- `11_chat_prompt_template.py` - Chat prompt templates
- `12_message_place_holder.py` - Message placeholders

#### 06_output_parsers
- `13_typed_dictionary.py` - TypedDict output parsing
- `14_structured_output_typed_dict.py` - Structured output with TypedDict
- `15_using_ollama_model.py` - Using Ollama models
- `16_pydantic.py` - Pydantic models
- `17_structured_output_pydantic.py` - Structured output with Pydantic
- `18_simple_output.py` - Simple output parsing
- `19_str_output_parser.py` - String output parser
- `20_json_output_parser.py` - JSON output parser
- `21_pydantic_output_parser.py` - Pydantic output parser

#### 07_chains
- `22_simple_chain.py` - Basic chain composition
- `23_sequential_chains.py` - Sequential chain execution
- `24_parallel_chains.py` - Parallel chain execution
- `25_conditional_chains.py` - Conditional chain logic

#### 08_Runnables
- `26_runnables_sequence.py` - Runnable sequences
- `27_runnables_parallel.py` - Parallel runnables
- `28_runnables_passthrough.py` - Passthrough runnables
- `29_runnables_lambda.py` - Lambda runnables
- `30_runnables_branch.py` - Branch runnables
- `31_runnables_branch_lcel.py` - Branch runnables with LCEL
- `32_runnables_parallel_lcel.py` - Parallel runnables with LCEL

---

### 02-RAG

Retrieval-Augmented Generation (RAG) system implementation.

#### 09_documents_loader
- `33_text_file_loader.py` - Load text files
- `34_pdf_loader.py` - Load PDF documents
- `35_directory_loader.py` - Load documents from directories
- `36_web_based_loader.py` - Load content from web sources
- `37_blog_question_answer.py` - Q&A from blog content
- `38_csv_loader.py` - Load CSV files

#### 10_text_splitters
- `39_length_based.py` - Length-based text splitting
- `40_length_based_doc_loader.py` - Document loading with length-based splitting
- `41_text_structure_based.py` - Structure-aware text splitting
- `42_text_structure_based_on_code.py` - Code-aware text splitting
- `43_semantic_text_splitters.py` - Semantic text splitting

#### 11_vector_stores
- `44_chroma.py` - Chroma vector store integration
- `44_chroma.ipynb` - Chroma notebook example

#### 12_retrievers
- `45_wikipedia_retriever.py` - Wikipedia retriever
- `46_vector_store_retriever.py` - Vector store retriever
- `47_mmr.py` - Maximum Marginal Relevance retriever
- `48_multiquery_retriever.py` - Multi-query retriever
- `49_contextual_compression_retriever.py` - Contextual compression retriever

#### 13_rag_system
Complete RAG system implementation:
- `text_splitter_51.py` - Text splitting component
- `youtube_transcript_loader_50.py` - YouTube transcript loader
- `embeddings_vector_store_52.py` - Embeddings and vector store setup
- `retriever_53.py` - Retriever configuration
- `prompt_context_54.py` - Context-aware prompts
- `model_55.py` - Model configuration
- `final_chain_56.py` - Final chain composition
- `main_57.ipynb` - Jupyter notebook example
- `main_58.py` - Main script
- `README.md` - RAG system documentation

---

### 03-Agents

Agent and autonomous systems implementation.

---

### Additional Files

- `main.py` - Main entry point
- `chat_history.txt` - Chat conversation history
- `drug200.csv` - Sample drug dataset
- `file.csv` - Sample CSV file
- `file.txt` - Sample text file
- `prompt_template.json` - Prompt template configuration
- `pyproject.toml` - Project dependencies and configuration

### books

Reference materials and resources.

---

## Running Examples

Run a script directly:

```bash
python 01-Fundamentals/01_models_define/01_chat_model.py
```

Or run a notebook:

```bash
jupyter notebook 02-RAG/13_rag_system/main_57.ipynb
```

## Notes

- Keep your API keys out of source control.
- Scripts are incremental; later examples may build on earlier concepts.
- Each file is designed to be runnable independently within its section.
- Review comments in scripts for detailed explanations of concepts.

## License

For learning and personal practice.
