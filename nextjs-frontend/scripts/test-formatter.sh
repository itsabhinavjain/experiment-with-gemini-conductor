#!/bin/bash
echo "Testing log formatter..."
echo "Line 1" | node nextjs-frontend/scripts/log-formatter.js
echo "Line 2" | node nextjs-frontend/scripts/log-formatter.js
