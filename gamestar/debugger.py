from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional


ERROR_EXPLANATIONS: Dict[str, str] = {
    "TypeError": "You used incompatible data types together.",
    "NameError": "You used a variable that does not exist.",
    "IndexError": "You tried to access something that is out of range.",
    "KeyError": "You tried to access a key that does not exist.",
    "ValueError": "You used the right type but wrong value.",
    "AttributeError": "The object does not have that attribute.",
    "FileNotFoundError": "A required file path does not exist.",
    "ZeroDivisionError": "You attempted to divide by zero.",
}


def explain_error(error: BaseException) -> str:
    error_type = type(error).__name__
    explanation = ERROR_EXPLANATIONS.get(error_type, "Unknown error occurred.")

    return (
        "\nGamestar Debug Report\n"
        f"Error Type: {error_type}\n"
        f"Explanation: {explanation}\n"
        f"Original Error: {error}\n"
    )


def run_file(filename: str) -> Optional[str]:
    path = Path(filename)
    try:
        source = path.read_text(encoding="utf-8")
        compiled = compile(source, str(path), "exec")
        exec_globals = {"__name__": "__main__"}
        exec(compiled, exec_globals)
        return None
    except Exception as error:  # noqa: BLE001
        report = explain_error(error)
        print(report)
        return report
