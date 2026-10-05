"""Load data science packages and analyze simulated Matrix data.

Checks which dependencies are installed, explains how to install the
missing ones with pip or Poetry, then generates data with numpy,
analyzes it with pandas and saves a chart with matplotlib.
"""

import importlib
import importlib.metadata
import sys

REQUIRED: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}
DATA_POINTS = 1000
OUTPUT_FILE = "matrix_analysis.png"


def get_version(package: str) -> str | None:
    """Return the installed version of a package, or None if missing."""
    try:
        importlib.import_module(package)
        return importlib.metadata.version(package)
    except (ImportError, importlib.metadata.PackageNotFoundError):
        return None


def check_dependencies() -> dict[str, str | None]:
    """Print the status of each required package and return versions."""
    print("Checking dependencies:")
    versions: dict[str, str | None] = {}
    for package, role in REQUIRED.items():
        version = get_version(package)
        versions[package] = version
        if version is None:
            print(f"[MISSING] {package} - {role} unavailable")
        else:
            print(f"[OK] {package} ({version}) - {role} ready")
    return versions


def detect_manager() -> str:
    """Guess which tool manages the environment running this script."""
    if sys.prefix == sys.base_prefix:
        return "none (global Python)"
    if "pypoetry" in sys.prefix:
        return "Poetry"
    return "pip (manual virtual environment)"


def compare_managers(versions: dict[str, str | None]) -> None:
    """Show installed versions and how pip and Poetry differ."""
    print("\nPackage manager comparison:")
    print(f"Active environment manager: {detect_manager()}")
    print(f"Environment path: {sys.prefix}")
    for package, version in versions.items():
        print(f"  {package:<12} {version or 'not installed'}")
    print("pip    -> reads requirements.txt, installs into the active env,")
    print("          you create and activate the venv yourself")
    print("Poetry -> reads pyproject.toml, creates its own venv,")
    print("          pins exact versions in poetry.lock")


def show_install_help() -> None:
    """Explain how to install the missing packages with pip or Poetry."""
    print("\nSome programs failed to load. Install them with:")
    print("\npip:")
    print("  python3 -m venv matrix_env")
    print("  source matrix_env/bin/activate")
    print("  pip install -r requirements.txt")
    print("  python3 loading.py")
    print("\nPoetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def run_analysis() -> None:
    """Generate Matrix data, analyze it and save a chart."""
    np = importlib.import_module("numpy")
    pd = importlib.import_module("pandas")
    plt = importlib.import_module("matplotlib.pyplot")

    # 1. Generate: 1000 random signal values around 50 (numpy)
    print("\nAnalyzing Matrix data...")
    print(f"Processing {DATA_POINTS} data points...")
    rng = np.random.default_rng(seed=42)
    data = pd.DataFrame({"signal": rng.normal(50, 15, DATA_POINTS)})

    # 2. Analyze: flag unusually strong signals as anomalies (pandas)
    data["anomaly"] = data["signal"] > 80
    print(f"Average signal: {data['signal'].mean():.2f}")
    print(f"Anomalies detected: {data['anomaly'].sum()}")

    # 3. Visualize: plot the signal and save it as an image (matplotlib)
    print("Generating visualization...")
    plt.plot(data["signal"], color="green")
    plt.title("Matrix signal strength")
    try:
        plt.savefig(OUTPUT_FILE)
    except OSError as error:
        print(f"ERROR: could not save chart: {error}")
        sys.exit(1)
    print("\nAnalysis complete!")
    print(f"Results saved to: {OUTPUT_FILE}")


def main() -> None:
    """Check dependencies, then run the analysis if possible."""
    print("LOADING STATUS: Loading programs...\n")
    versions = check_dependencies()
    if None in versions.values():
        show_install_help()
        sys.exit(1)
    compare_managers(versions)
    run_analysis()


if __name__ == "__main__":
    main()
