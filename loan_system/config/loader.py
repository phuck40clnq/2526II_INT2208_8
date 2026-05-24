import yaml
from pathlib import Path


CONFIG_DIR = Path(__file__).parent


def load_yaml(path: str) -> dict[str, str]:
    path = CONFIG_DIR / path

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
    
def load_test(filename: str) -> dict[str, str]:
    load_yaml(f"test_cases/{filename}")
