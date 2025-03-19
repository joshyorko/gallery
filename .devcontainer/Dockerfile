FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Copy first run notice
COPY first-run-notice.txt /tmp/scripts/

# Add setup script
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  gcc \
  g++ \
  make \
  libc6 \
  libstdc++6 \
  bash \
  git \
  curl \
  wget \
  vim \
  nano \
  zip \
  unzip \
  xclip \
  python3.12-venv \
  # Browser dependencies
  libasound2t64 \
  libatk1.0-0 \
  libatk-bridge2.0-0 \
  libcups2 \
  libdbus-1-3 \
  libdrm2 \
  libgbm1 \
  libgtk-3-0 \
  libnspr4 \
  libnss3 \
  libx11-6 \
  libxcb1 \
  libxcomposite1 \
  libxdamage1 \
  libxext6 \
  libxfixes3 \
  libxrandr2 \
  libxshmfence1 \
  && \
  rm -rf /var/lib/apt/lists/*

# Download Sema4.ai Action Server, Agent CLI, and RCC
RUN curl -o action-server https://cdn.sema4.ai/action-server/releases/latest/linux64/action-server && \
    chmod a+x action-server && \
    sudo mv action-server /usr/local/bin/ && \
    curl -o agent-cli https://cdn.sema4.ai/agent-cli/releases/latest/linux64/agent-cli && \
    chmod a+x agent-cli && \
    sudo mv agent-cli /usr/local/bin/ && \
    curl -o rcc https://cdn.sema4.ai/rcc/releases/latest/linux64/rcc && \
    chmod a+x rcc && \
    sudo mv rcc /usr/local/bin/

# Move first run notice
RUN sudo mkdir -p "/usr/local/etc/vscode-dev-containers/" && \
  sudo mv -f /tmp/scripts/first-run-notice.txt /usr/local/etc/vscode-dev-containers/

CMD ["sleep", "infinity"]