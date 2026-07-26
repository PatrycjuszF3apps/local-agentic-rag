#!/bin/bash
set -e
echo "Updating Python and Node.js runtimes..."
apt-get update && apt-get install --only-upgrade -y python3 nodejs
echo "Updating npm..."
npm install -g npm@latest
echo "Runtimes update complete."
