import pytest

from src.decorators import log


def test_log_success(tmp_path):
    """Тест успешного выполнения"""
    log_file = tmp_path / "log_success.txt"

    @log(filename=str(log_file))
    def my_func(a, b):
        return a + b

    my_func(1, 2)

    assert log_file.read_text(encoding="utf-8").strip() == "my_func ok"


def test_log_error(tmp_path):
    """Тест ошибки"""
    log_file = tmp_path / "log_error.txt"

    @log(filename=str(log_file))
    def my_func(a, b):
        raise RuntimeError("error")

    with pytest.raises(RuntimeError):
        my_func(1, 2)

    assert (
        log_file.read_text(encoding="utf-8").strip()
        == "my_func error: RuntimeError. Inputs: (1, 2), {}"
    )


def test_log_console_basic(capsys):
    """Тест консольного вывода"""

    @log()
    def test_func():
        return "ok"

    test_func()
    assert capsys.readouterr().out.strip() == "test_func ok"


def test_log_different_error_types():
    """Тестируем разные типы ошибок"""
    error_types = [ValueError, TypeError, RuntimeError, ZeroDivisionError]

    for error_type in error_types:
        @log()
        def my_func():
            raise error_type("test")

        with pytest.raises(error_type):
            my_func()
