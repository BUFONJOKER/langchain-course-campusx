## LangChain Course Practice

This repo contains small, focused scripts and notes created while following a LangChain course. Each file is meant to be run standalone so you can explore one concept at a time.

## What's Inside

- `01_chat_model.py` - Basic chat model usage example.
- `02_embeddings_model.py` - Embeddings model usage example.

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

## Run Examples

Run a script directly:

```bash
python 01_chat_model.py
```

## Notes

- Keep your API keys out of source control.
- Scripts are incremental and may assume earlier concepts.

## License

For learning and personal practice.
