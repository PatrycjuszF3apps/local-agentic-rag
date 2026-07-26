#!/bin/bash
set -e
echo "Updating Python RAG dependencies..."
VENV_PATH="/home/local-agentic-rag/.venv"
"$VENV_PATH/bin/pip" install --upgrade --no-cache-dir lancedb pandas sentence-transformers pypdf python-docx python-pptx beautifulsoup4 openpyxl odfpy
echo "RAG dependencies update complete."
