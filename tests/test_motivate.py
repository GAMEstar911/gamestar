import pytest

from gamestar.motivate import motivate


def test_motivate_returns_selected_message(capsys) -> None:
    message = motivate(messages=("Keep going.",))
    output = capsys.readouterr().out

    assert message == "Keep going."
    assert "Gamestar says:" in output
    assert "Keep going." in output


def test_motivate_rejects_empty_messages() -> None:
    with pytest.raises(ValueError, match="at least one"):
        motivate(messages=())
