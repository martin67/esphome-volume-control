from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
VENV = ROOT / ".venv"

IS_WINDOWS = sys.platform.startswith("win")

if IS_WINDOWS:
    VENV_PYTHON = VENV / "Scripts" / "python.exe"
else:
    VENV_PYTHON = VENV / "bin" / "python"


def run(cmd):
    print(">>", " ".join(map(str, cmd)))
    subprocess.check_call(cmd)


def create_venv():
    if VENV.exists():
        print("✔ .venv already exists")
        return

    print("Creating virtual environment...")
    run([sys.executable, "-m", "venv", str(VENV)])


def install_dependencies():
    if not VENV_PYTHON.exists():
        raise RuntimeError("Virtual environment python not found")

    req = ROOT / "requirements.txt"

    if not req.exists():
        print("No requirements.txt found — skipping dependency install")
        return

    print("Upgrading pip...")
    run([str(VENV_PYTHON), "-m", "pip", "install", "--upgrade", "pip"])

    print("Installing dependencies...")
    run([str(VENV_PYTHON), "-m", "pip", "install", "-r", str(req)])


def verify():
    print("\n=== Verification ===")
    run([str(VENV_PYTHON), "-c", "import sys; print(sys.executable)"])


def main():
    print("=== Bootstrap ESPHome Project ===\n")

    create_venv()
    install_dependencies()
    verify()

    print("\n✔ Bootstrap complete")
    print("Next step:")
    print("  - Open VS Code")
    print("  - Select interpreter: .venv (if not auto-detected)")
    print("  - Run diagram tasks (Ctrl+Shift+B)")


if __name__ == "__main__":
    main()
    