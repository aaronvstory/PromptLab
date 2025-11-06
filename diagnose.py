#!/usr/bin/env python
"""Quick diagnostic script to identify the issue"""
import sys

print("=== PromptLab Diagnostic ===\n")

# Test 1: Python version
print(f"✓ Python {sys.version}")

# Test 2: Streamlit import
try:
    import streamlit as st
    print(f"✓ Streamlit {st.__version__} imported")
except Exception as e:
    print(f"✗ Streamlit import failed: {e}")
    sys.exit(1)

# Test 3: Google AI import
try:
    import google.generativeai as genai
    print("✓ Google GenAI imported")
except Exception as e:
    print(f"✗ Google GenAI import failed: {e}")
    sys.exit(1)

# Test 4: Secrets file
try:
    from pathlib import Path
    secrets_file = Path(".streamlit/secrets.toml")
    if secrets_file.exists():
        print(f"✓ secrets.toml exists ({secrets_file.stat().st_size} bytes)")
    else:
        print("✗ secrets.toml not found")
        sys.exit(1)
except Exception as e:
    print(f"✗ Error checking secrets: {e}")
    sys.exit(1)

# Test 5: API key format
try:
    import toml
    secrets = toml.load(".streamlit/secrets.toml")
    api_key = secrets.get("GEMINI_API_KEY", "")
    if api_key and api_key.startswith("AIza"):
        print(f"✓ API key present (starts with AIza...)")
    else:
        print(f"✗ API key invalid format")
        sys.exit(1)
except Exception as e:
    print(f"✗ Error reading API key: {e}")

# Test 6: Port availability
import socket
port = 8501
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    if s.connect_ex(('localhost', port)) == 0:
        print(f"✗ Port {port} is ALREADY IN USE!")
        print("  Try running: netstat -ano | findstr :8501")
        print("  Or use different port: streamlit run app.py --server.port 8502")
    else:
        print(f"✓ Port {port} is available")

print("\n=== All checks passed! ===")
print("\nTry running:")
print("  streamlit run app.py --server.headless false")
