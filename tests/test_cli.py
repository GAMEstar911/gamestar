from pathlib import Path

from gamestar.cli import main


def test_cli_scan_returns_nonzero_for_findings(tmp_path: Path, capsys) -> None:
    target = tmp_path / "risky.py"
    target.write_text('password = "123"\n', encoding="utf-8")

    exit_code = main(["scan", str(target)])
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "Gamestar Security Report" in output


def test_cli_scan_returns_zero_for_clean_file(tmp_path: Path) -> None:
    target = tmp_path / "clean.py"
    target.write_text("print('safe')\n", encoding="utf-8")

    exit_code = main(["scan", str(target)])

    assert exit_code == 0


def test_cli_run_returns_nonzero_on_exception(tmp_path: Path) -> None:
    target = tmp_path / "broken.py"
    target.write_text("x = []\nprint(x[1])\n", encoding="utf-8")

    exit_code = main(["run", str(target)])

    assert exit_code == 1


def test_cli_motivate_returns_zero() -> None:
    exit_code = main(["motivate"])
    assert exit_code == 0
