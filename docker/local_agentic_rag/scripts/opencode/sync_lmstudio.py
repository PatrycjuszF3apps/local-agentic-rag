import urllib.request
import json
import os
import sys

# Address configuration
if len(sys.argv) > 1 and sys.argv[1]:
    base_url = sys.argv[1]
else:
    base_url = os.environ.get("LM_STUDIO_API_BASE_URL")

if not base_url:
    print("Error: Base URL not provided (neither as an argument nor in the environment variable).")
    exit(1)

base_url = base_url.rstrip("/")
models_url = f"{base_url}/api/v0/models"
chat_url = f"{base_url}/v1"

CONFIG_PATH = os.path.expanduser("opencode.json")

print(f"Fetching model list from LM Studio (API v0) at {models_url}...")
try:
    with urllib.request.urlopen(models_url) as response:
        data = json.loads(response.read().decode())
        models_data = data.get("data", [])
except Exception as e:
    print(f"Connection error: {e}\nEnsure that the LM Studio server is running on the host.")
    exit(1)

# Formatting models for OpenCode
models_dict = {}
for m in models_data:
    model_id = m.get("id")
    model_type = m.get("type", "llm") # Default to llm as fallback
    
    # Skip embedding models, as they are not used for chat
    if model_type == "embeddings":
        continue

    # If the API returns the "vlm" type, the model supports image analysis
    input_modalities = ["text", "image"] if model_type == "vlm" else ["text"]

    models_dict[model_id] = {
        "name": model_id,
        "modalities": {
            "input": input_modalities,
            "output": ["text"]
        }
    }

print(f"Found {len(models_dict)} chat/VLM models.")

# Read the current opencode.json file (or create a new one)
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
else:
    config = {}
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)

# Build the appropriate structure in JSON
if "provider" not in config:
    config["provider"] = {}

if "lmstudio" not in config["provider"]:
    config["provider"]["lmstudio"] = {
        "npm": "@ai-sdk/openai-compatible",
        "name": "LM Studio (Host)",
        "options": {}
    }

if "options" not in config["provider"]["lmstudio"]:
    config["provider"]["lmstudio"]["options"] = {}

# Update baseURL
config["provider"]["lmstudio"]["options"]["baseURL"] = chat_url

# Inject fetched models
config["provider"]["lmstudio"]["models"] = models_dict

# Save to file
with open(CONFIG_PATH, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)

print(f"Success! Updated file: {CONFIG_PATH}")
