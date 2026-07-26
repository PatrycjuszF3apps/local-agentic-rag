# Dockerfile – Ubuntu 26.04
FROM ubuntu:26.04

# Arguments from .env
ARG UID=1000
ARG GID=1000

SHELL ["/bin/bash", "-c"]

# 1. CHANGE: Set TERM to xterm-256color to force color support in terminal
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 LC_ALL=C.UTF-8 \
    TERM=xterm-256color

# Basic system tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gnupg2 curl wget ca-certificates python3-virtualenv  python3.14-venv  \
        build-essential mc nano \
        && rm -rf /var/lib/apt/lists/*

# Install Node.js 22.x (LTS)
RUN curl -fsSL https://deb.nodesource.com/setup_26.x | bash - && \
    apt-get install -y nodejs


# USER MANAGEMENT
# First remove default "ubuntu" user (UID 1000)
RUN userdel -r ubuntu || true
RUN groupdel ubuntu || true

# Create group and user "local-agentic-rag" cleanly
RUN groupadd -g ${GID} local-agentic-rag
RUN useradd -u ${UID} -g ${GID} -m -s /bin/bash local-agentic-rag

# Enable color prompt in .bashrc
# Uncomment 'force_color_prompt=yes' line in user config file
RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' /home/local-agentic-rag/.bashrc

# Add useful aliases (e.g., 'll' as detailed list)
RUN echo "alias ll='ls -alF'" >> /home/local-agentic-rag/.bashrc

# Set working directory
WORKDIR /app

# Switch to user
USER local-agentic-rag

# Create directories for named volumes to ensure proper ownership
RUN mkdir -p /home/local-agentic-rag/.opencode \
    /home/local-agentic-rag/.config/opencode \
    /home/local-agentic-rag/.cache/opencode \
    /home/local-agentic-rag/agent \
    /home/local-agentic-rag/.cache/huggingface

# Copy scripts directory
COPY --chown=local-agentic-rag:local-agentic-rag scripts /home/local-agentic-rag/.local/bin/scripts
RUN chmod -R +x /home/local-agentic-rag/.local/bin/scripts

# Install OpenCode
RUN /home/local-agentic-rag/.local/bin/scripts/opencode/install.sh

# Install LanceDB & RAG Dependencies
RUN /home/local-agentic-rag/.local/bin/scripts/lancedb/install.sh

COPY --chown=local-agentic-rag:local-agentic-rag rootfs/ /
# Set working directory
WORKDIR /app

# Start command
CMD ["/bin/bash"]