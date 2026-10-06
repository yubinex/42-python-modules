"""Detect whether Python runs inside a virtual environment.

Prints details about the current interpreter and where packages are
installed, or explains how to create a venv if none is active.
"""

import os
import site
import sys


def is_in_venv() -> bool:
    """Return True if the running Python belongs to a virtual environment.

    Inside a venv, sys.prefix points to the venv folder while
    sys.base_prefix still points to the original Python installation.
    """
    return sys.prefix != sys.base_prefix


def get_global_site_packages() -> str:
    """Return the site-packages path of the global Python installation.

    Built from sys.base_prefix so it stays correct inside a venv.
    """
    version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    return os.path.join(sys.base_prefix, "lib", version, "site-packages")


def show_outside_matrix() -> None:
    """Print the global environment status and venv setup steps."""
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")
    print("\nGlobal package installation path:")
    print(get_global_site_packages())


def show_inside_construct() -> None:
    """Print the venv details and compare its path to the global one."""
    venv_path = sys.prefix
    venv_name = os.path.basename(venv_path)
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(site.getsitepackages()[0])
    print("\nGlobal package path (not used here):")
    print(get_global_site_packages())


def main() -> None:
    """Show the status that matches the current environment."""
    if is_in_venv():
        show_inside_construct()
    else:
        show_outside_matrix()


if __name__ == "__main__":
    main()
