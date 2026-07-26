#!/bin/bash
set -e
echo "Updating OS packages..."
apt-get update && apt-get upgrade -y
echo "System update complete."
