from typing import Any

import pytest

from src.decorators import my_function


def test_my_function(capsys: Any) -> None:
    """Проверка корректной работы вывода информации."""
    my_function(1, 3)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_my_function_error(capsys: Any) -> None:
    """Проверка корректной работы вывода информации с ошибкой."""
    with pytest.raises(TypeError):
        my_function(1, "8")
    captured_error = capsys.readouterr()
    assert captured_error.out == (
        "my_function error: unsupported operand type(s) for +: " "'int' and 'str'. Inputs: (1, '8'), {}.\n"
    )
