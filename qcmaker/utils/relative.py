from pathlib import Path

def get(__file__: str, file: str) -> str:
    return str(Path(__file__).parent / file)