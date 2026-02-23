from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable, List, Sequence


@dataclass(frozen=True)
class ScanFinding:
    line: int
    rule: str
    message: str


PASSWORD_ASSIGNMENT_PATTERN = re.compile(
    r"\b(password|passwd|pwd|secret|token)\b\s*=\s*['\"]", re.IGNORECASE
)
EXEC_PATTERN = re.compile(r"\bexec\s*\(")
EVAL_PATTERN = re.compile(r"\beval\s*\(")


def _scan_lines(lines: Sequence[str]) -> List[ScanFinding]:
    findings: List[ScanFinding] = []

    for line_number, line in enumerate(lines, start=1):
        if PASSWORD_ASSIGNMENT_PATTERN.search(line):
            findings.append(
                ScanFinding(
                    line=line_number,
                    rule="hardcoded-secret",
                    message="Hardcoded secret assignment detected.",
                )
            )
        if EXEC_PATTERN.search(line):
            findings.append(
                ScanFinding(
                    line=line_number,
                    rule="dynamic-exec",
                    message="exec() can execute arbitrary code and is dangerous.",
                )
            )
        if EVAL_PATTERN.search(line):
            findings.append(
                ScanFinding(
                    line=line_number,
                    rule="dynamic-eval",
                    message="eval() can execute arbitrary code and is dangerous.",
                )
            )

    return findings


def format_scan_report(findings: Iterable[ScanFinding]) -> str:
    finding_list = list(findings)
    if not finding_list:
        return "Gamestar Security Report: No risks detected"

    lines = ["Gamestar Security Report:"]
    for finding in finding_list:
        lines.append(f"- Line {finding.line} [{finding.rule}]: {finding.message}")
    return "\n".join(lines)


def scan_file(filename: str, print_report: bool = True) -> List[ScanFinding]:
    path = Path(filename)
    file_contents = path.read_text(encoding="utf-8")
    findings = _scan_lines(file_contents.splitlines())
    if print_report:
        print(format_scan_report(findings))
    return findings
