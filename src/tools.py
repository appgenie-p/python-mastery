from pathlib import Path


def get_path(relative_path: str) -> str:
    module_dir = Path(__file__).resolve().parent.parent
    path = module_dir / relative_path
    return str(path)

