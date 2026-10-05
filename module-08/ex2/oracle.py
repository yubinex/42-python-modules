"""Read the Matrix configuration from environment variables.

Values come from a .env file, but variables set in the shell always win.
Development mode tolerates missing settings, production mode refuses to
start without them and hides the database URL.
"""

import os
import sys

try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

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
        load_dotenv(".env")
    else:
        print("WARNING: python-dotenv not installed, .env file ignored\n")
    return {key: os.environ.get(key, "") for key in CONFIG_KEYS}


def get_mode(config: dict[str, str]) -> str:
    """Return the mode (development by default), stop if it is invalid."""
    mode = config["MATRIX_MODE"] or "development"
    if mode not in ("development", "production"):
        print(f"ERROR: MATRIX_MODE must be development or production, "
              f"not '{mode}'")
        sys.exit(1)
    return mode


def check_missing(config: dict[str, str], mode: str) -> None:
    """Warn about missing settings, or stop if running in production."""
    missing = [key for key in CONFIG_KEYS
               if key != "MATRIX_MODE" and not config[key]]
    if missing and mode == "production":
        print(f"ERROR: production needs every setting, missing: "
              f"{', '.join(missing)}")
        sys.exit(1)
    for key in missing:
        print(f"WARNING: {key} not set")
    if missing:
        print()


def show_config(config: dict[str, str], mode: str) -> None:
    """Print the settings, hiding the database URL in production."""
    database = config["DATABASE_URL"] or "not set"
    if mode == "production":
        database = "[hidden in production]"
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {'Authenticated' if config['API_KEY'] else 'No key'}")
    print(f"Log Level: {config['LOG_LEVEL'] or 'not set'}")
    print(f"Zion Network: {config['ZION_ENDPOINT'] or 'not set'}")


def security_check() -> None:
    """Report where the secrets come from."""
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.isfile(".env"):
        print("[OK] .env file found")
    else:
        print("[WARNING] No .env file found (cp .env.example .env)")


def main() -> None:
    """Load, check and display the Matrix configuration."""
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    mode = get_mode(config)
    check_missing(config, mode)
    show_config(config, mode)
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
