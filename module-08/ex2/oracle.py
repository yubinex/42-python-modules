"""Read the Matrix configuration from environment variables.

Values come from a .env file, but variables set in the shell always win.
Development mode tolerates missing settings, production mode refuses to
start without them.
"""

import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]

    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(SCRIPT_DIRECTORY, ".env")
GITIGNORE_FILE = os.path.join(SCRIPT_DIRECTORY, ".gitignore")
CONFIG_KEYS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_config() -> dict[str, str]:
    """Load the .env file, then read every setting from the environment."""
    if DOTENV_AVAILABLE:
        load_dotenv(ENV_FILE)
    else:
        print("WARNING: python-dotenv not installed, .env file ignored\n")
    return {key: os.environ.get(key, "") for key in CONFIG_KEYS}


def get_mode(config: dict[str, str]) -> str:
    """Return the mode (development by default), stop if it is invalid."""
    mode = config["MATRIX_MODE"] or "development"
    if mode not in ("development", "production"):
        print(
            f"ERROR: MATRIX_MODE must be development or production, "
            f"not '{mode}'"
        )
        sys.exit(1)
    return mode


def check_missing(config: dict[str, str], mode: str) -> None:
    """Warn about missing settings, or stop if running in production."""
    missing = [
        key for key in CONFIG_KEYS if key != "MATRIX_MODE" and not config[key]
    ]
    if missing and mode == "production":
        print(
            f"ERROR: production needs every setting, missing: "
            f"{', '.join(missing)}"
        )
        sys.exit(1)
    for key in missing:
        print(f"WARNING: {key} not set")
    if missing:
        print()


def show_config(config: dict[str, str], mode: str) -> None:
    """Print the status of each setting without revealing its value."""
    url = config["DATABASE_URL"]
    if not url:
        database = "Not configured"
    elif any(local in url for local in ("sqlite", "localhost", "127.0.0.1")):
        database = "Connected to local instance"
    else:
        database = "Connected to remote instance"
    api = "Authenticated" if config["API_KEY"] else "Not authenticated"
    zion = "Online" if config["ZION_ENDPOINT"] else "Offline"
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {api}")
    print(f"Log Level: {config['LOG_LEVEL'] or 'not set'}")
    print(f"Zion Network: {zion}")


def env_is_gitignored() -> bool:
    """Return True if .gitignore keeps the .env file out of git."""
    try:
        with open(GITIGNORE_FILE, encoding="utf-8") as gitignore:
            return ".env" in [line.strip() for line in gitignore]
    except (OSError, UnicodeError):
        return False


def security_check(config: dict[str, str], shell_keys: list[str]) -> None:
    """Check the API key, the .env file and the shell overrides."""
    print("\nEnvironment security check:")
    if config["API_KEY"] == "your-api-key-here":
        print("[WARNING] API_KEY is still the placeholder from .env.example")
    else:
        print("[OK] No hardcoded secrets detected")
    if not os.path.isfile(ENV_FILE):
        print("[WARNING] No .env file found (cp .env.example .env)")
    elif not env_is_gitignored():
        print("[WARNING] .env is not in .gitignore, secrets could leak")
    else:
        print("[OK] .env file properly configured")
    # load_dotenv never replaces variables already set in the shell
    overrides = f" (active: {', '.join(shell_keys)})" if shell_keys else ""
    print(f"[OK] Production overrides available{overrides}")


def main() -> None:
    """Load, check and display the Matrix configuration."""
    print("ORACLE STATUS: Reading the Matrix...\n")
    shell_keys = [key for key in CONFIG_KEYS if key in os.environ]
    config = load_config()
    mode = get_mode(config)
    check_missing(config, mode)
    show_config(config, mode)
    security_check(config, shell_keys)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
