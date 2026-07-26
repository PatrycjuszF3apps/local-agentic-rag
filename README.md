# Local Agentic RAG

A local, serverless Retrieval-Augmented Generation (RAG) system utilizing [LanceDB](https://lancedb.com/) and SentenceTransformers. It is designed to seamlessly integrate with OpenCode CLI, providing autonomous, deep investigative capabilities over your local documents without relying on external cloud APIs for embedding.

## Features

- **Local & Serverless:** Uses LanceDB for lightweight, serverless vector storage directly on your filesystem.
- **Extensive File Support:** Automatically extracts, chunks, and embeds text from a wide range of formats including PDF, DOCX, PPTX, CSV, XLSX, ODS, HTML, TXT, MD, ODT, and ODP.
- **Deep Investigative Agent:** Includes `rag-deep`, an OpenCode autonomous investigator that translates natural language queries into semantic keywords and iteratively drills down into the database to synthesize comprehensive answers.
- **Dockerized Environment:** A pre-configured Docker setup (Ubuntu, Python, Node.js) ensures a consistent workspace and execution environment.

## LM Studio Integration

This project was built with a core philosophy of 100% local, and cost-free execution. By integrating [LM Studio](https://lmstudio.ai/), a popular and user-friendly local LLM runner, the system remains completely independent of paid cloud providers (like OpenAI or Anthropic). You can run powerful agentic queries on your own hardware.

**Model Requirements:**
- The model loaded in LM Studio **must support tool calling** (often labeled as "tools").
- Please note that local models, especially heavily compressed or quantized ones, may struggle with complex agentic tasks and could behave incorrectly or produce unreliable results.

## OpenCode Integration

This project bundles the open-source **OpenCode** CLI to act as the primary interface and intelligent orchestrator. The main advantages of this integration include:
- **Seamless Communication:** It acts as a perfect bridge between the user's natural language, the LM Studio models, and the local LanceDB vector database.
- **Agentic Capabilities:** OpenCode powers the `rag-deep` agent, allowing the LLM to autonomously formulate search strategies, execute Python queries, and iteratively gather context without constant human prompting.
- **Interactive Experience:** It provides a rich, terminal-based environment tailored for complex research and data extraction right out of the box.

## Configuration

It is highly recommended to override default variables from `docker-compose.yml` by creating a `docker-compose.override.yml` file. This ensures your local settings remain intact when pulling project updates.

To configure your connection to LM Studio, simply copy the provided example file:

```bash
cp docker-compose.override.yml.example docker-compose.override.yml
```

Then, open `docker-compose.override.yml` and follow the instructions inside to set your actual IP address and port.

## Usage

> **Note:** The following startup instructions apply to Unix-like environments. The application has been specifically tested and verified to run on Windows Subsystem for Linux 2 (WSL2).

1. **Ingestion:** Place your source documents in the `app/_raw_input/` directory.
   - *Recommendation:* When starting out, avoid dropping a massive amount of files or extremely heavy files all at once. First, test your local machine's capabilities by executing `task rag:sync` on a small sample of documents. Once you understand your hardware's performance and embedding speed, you can confidently process larger batches.
2. **Processing:** The system will automatically ingest, chunk, and embed the documents using the `all-MiniLM-L6-v2` model upon the next sync or search execution. Processed files are moved to `app/_raw_input/.processed/`.
3. **Investigation:** Use the OpenCode CLI (`rag-deep` command) or run `rag.py` directly to perform semantic searches and gather insights from your local database.

### Taskfile Commands

- `task build` / `task build-no-cache`: Recreate and build the containers.
- `task up` / `task down`: Start or stop the services.
- `task log`: Print and follow container logs on the standard output.
- `task opencode:sync`: Synchronize available LM Studio models into the OpenCode configuration within the container.
- `task opencode:run`: Launch the OpenCode interactive CLI to start your agentic queries.
- `task rag:sync`: Synchronize and process documents for the RAG database.
- `task rag:wipe`: Wipe the LanceDB database and reset processed files.
- `task infrastructure:update-tools`: Update CLI tools (e.g. OpenCode) inside the container.
- `task infrastructure:update-runtimes`: Live update Python and Node.js runtimes.
- `task infrastructure:update-rag`: Update Python dependencies for the RAG environment.
- `task infrastructure:update-system`: Update all OS packages inside the container.
- `task infrastructure:update-base-image`: Pull the latest base images and fully rebuild the container.
- `task infrastructure:update-all`: Run all of the live infrastructure updates sequentially.

## TODO

- [ ] Implement a safeguard to prevent certain local models from falling into an infinite loop of executing `rag.py` calls.

## Important Notice

> **Disclaimer:** While this application is designed to run entirely locally, there is no absolute guarantee of security for the information or files inputted into the system. You are solely responsible for ensuring the safety, privacy, and confidentiality of the data you process using this software.

## License

This project is licensed under the [MIT License](LICENSE).
Copyright (c) 2026 Patrycjusz Marciniak.