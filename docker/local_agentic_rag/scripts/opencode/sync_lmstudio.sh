#!/bin/bash
# Script runs inside the container to sync LM Studio models and copy config

cd /home/local-agentic-rag/.local/bin/scripts/opencode || exit 1

echo "Running sync_lmstudio.py..."
python3 sync_lmstudio.py "$LM_STUDIO_API_BASE_URL"

echo "Copying generated opencode.json to ~/.opencode/opencode.json"
cp opencode.json ~/.opencode/opencode.json

echo "Sync complete!"
