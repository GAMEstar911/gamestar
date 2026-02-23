from pathlib import Path

from gamestar.scanner import format_scan_report, scan_file


def test_scan_file_detects_multiple_risks(tmp_path: Path, capsys) -> None:
    target = tmp_path / "risky.py"
    target.write_text(
        'password = "secret"\n'
        'token = "abcd"\n'
        "eval('1 + 1')\n"
        "exec('print(1)')\n",
        encoding="utf-8",
    )

    findings = scan_file(str(target))
    output = capsys.readouterr().out

    assert len(findings) == 4
    assert "hardcoded-secret" in output
    assert "dynamic-eval" in output
    assert "dynamic-exec" in output


def test_scan_file_clean_input(tmp_path: Path) -> None:
    target = tmp_path / "safe.py"
    target.write_text("print('ok')\n", encoding="utf-8")

    findings = scan_file(str(target), print_report=False)
    report = format_scan_report(findings)

    assert findings == []
    assert report == "Gamestar Security Report: No risks detected"
