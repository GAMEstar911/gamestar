from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, Optional

from gamestar import __version__
from gamestar.debugger import run_file
from gamestar.motivate import motivate
from gamestar.scanner import scan_file


def _existing_file(path_value: str) -> str:
    path = Path(path_value)
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"File not found: {path_value}")
    return str(path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gamestar",
        description="Gamestar developer assistant CLI.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan a file for risky patterns.")
    scan_parser.add_argument("file", type=_existing_file, help="Path to file to scan.")

    run_parser = subparsers.add_parser("run", help="Run a Python file with friendly errors.")
    run_parser.add_argument("file", type=_existing_file, help="Path to file to execute.")

    subparsers.add_parser("motivate", help="Print a short motivational message.")

    return parser


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "scan":
        findings = scan_file(args.file, print_report=True)
        return 1 if findings else 0

    if args.command == "run":
        report = run_file(args.file)
        return 1 if report else 0

    if args.command == "motivate":
        motivate()
        return 0

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
