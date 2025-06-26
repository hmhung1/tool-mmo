import requests
import tempfile
import subprocess
import sys
import os

url = "https://raw.githubusercontent.com/hmhung1/tool-mmo/refs/heads/main/obf-golikett.py"

code = requests.get(url).text

with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
    tmp.write(code)
    tmp.flush()
    filepath = tmp.name

try:
    subprocess.run([sys.executable, filepath], check=True)
finally:
    os.remove(filepath)