import sys
from pathlib import Path
from tempfile import TemporaryDirectory

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from gamestar import explain_error, motivate, run_file, scan_file


def _write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def main() -> None:
    with TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)

        risky_file = tmp / "risky_script.py"
        _write(
            risky_file,
            'password = "admin123"\n'
            'user_code = "print(2 + 2)"\n'
            "eval(user_code)\n",
        )

        clean_file = tmp / "clean_script.py"
        _write(clean_file, "print('Safe script')\n")

        valid_run_file = tmp / "valid_run.py"
        _write(valid_run_file, "print('Debug run success')\n")

        broken_run_file = tmp / "broken_run.py"
        _write(broken_run_file, "numbers = [1, 2, 3]\nprint(numbers[10])\n")

        print("=== 1) Security scanner (risky input) ===")
        scan_file(str(risky_file))
        print()

        print("=== 2) Security scanner (clean input) ===")
        scan_file(str(clean_file))
        print()

        print("=== 3) Debugger run_file (successful script) ===")
        run_file(str(valid_run_file))
        print()

        print("=== 4) Debugger run_file (failing script) ===")
        run_file(str(broken_run_file))
        print()

    print("=== 5) Debugger explain_error (direct usage) ===")
    try:
        int("not-a-number")
    except ValueError as error:
        print(explain_error(error))

    print("=== 6) Motivation helper ===")
    motivate()


if __name__ == "__main__":
    main()
