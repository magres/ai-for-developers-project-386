import subprocess, sys, os
from pathlib import Path

backend = Path(__file__).resolve().parent.parent / "backend"
venv = backend / ".venv"
python = venv / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")

if not python.exists():
    python = "python"

os.chdir(backend)
sys.exit(subprocess.call([str(python), "-m", "uvicorn", "app.main:app", "--reload", "--port", "8000"]))
