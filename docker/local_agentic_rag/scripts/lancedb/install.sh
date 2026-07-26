#!/bin/bash
set -e

echo "Starting Python environment configuration for LanceDB RAG..."

VENV_PATH="/home/local-agentic-rag/.venv"

# Create a virtual environment
python3 -m venv "$VENV_PATH"

# Upgrade pip
"$VENV_PATH/bin/pip" install --no-cache-dir --upgrade pip

# STEP 1: Install lightweight PyTorch (CPU only)
# This prevents downloading massive CUDA libraries, saving gigabytes of space and time.
echo "Installing PyTorch (CPU only)..."
"$VENV_PATH/bin/pip" install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# STEP 2: Install remaining dependencies
# pip will detect that torch is already installed and will skip downloading heavy GPU versions.
echo "Installing remaining RAG libraries..."
"$VENV_PATH/bin/pip" install --no-cache-dir \
    lancedb \
    pandas \
    sentence-transformers \
    pypdf \
    python-docx \
    python-pptx \
    beautifulsoup4 \
    openpyxl \
    odfpy

echo "RAG environment is ready at: $VENV_PATH"