from pathlib import Path

from gamestar.debugger import explain_error, run_file


def test_explain_error_returns_readable_report() -> None:
    report = explain_error(ValueError("bad"))

    assert "Gamestar Debug Report" in report
    assert "Error Type: ValueError" in report
    assert "right type but wrong value" in report


def test_run_file_success(tmp_path: Path, capsys) -> None:
    target = tmp_path / "ok.py"
    target.write_text("print('hello')\n", encoding="utf-8")

    report = run_file(str(target))
    output = capsys.readouterr().out

    assert report is None
    assert "hello" in output


def test_run_file_failure(tmp_path: Path, capsys) -> None:
    target = tmp_path / "broken.py"
    target.write_text("items = [1]\nprint(items[2])\n", encoding="utf-8")

    report = run_file(str(target))
    output = capsys.readouterr().out

    assert report is not None
    assert "IndexError" in report
    assert "Gamestar Debug Report" in output
