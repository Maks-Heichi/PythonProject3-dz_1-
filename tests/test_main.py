import builtins
import unittest
from unittest.mock import patch

from main import ALLOWED_STATUSES, main
from src.utils import load_transactions


class TestMainFlow(unittest.TestCase):
    """Интеграционный тест основного сценария main()."""

    @patch.object(builtins, "print")
    def test_main_json_executed_no_extra_filters(self, mock_print) -> None:
        # Последовательность ответов пользователя:
        # 1 – JSON, EXECUTED, потом три раза "нет" на дополнительные вопросы.
        user_inputs = iter(
            [
                "1",  # выбор JSON
                "EXECUTED",  # корректный статус
                "нет",  # сортировать по дате?
                "нет",  # только рублевые?
                "нет",  # фильтр по слову?
            ]
        )

        def fake_input(_prompt: str = "") -> str:
            return next(user_inputs)

        with patch.object(builtins, "input", side_effect=fake_input):
            main()

        # Проверяем, что итоговый вывод был вызван
        printed_text = " ".join(" ".join(map(str, call.args)) for call in mock_print.call_args_list)
        self.assertIn("Распечатываю итоговый список транзакций", printed_text)

        # Количество EXECUTED операций в JSON-файле должно совпадать с сообщением о количестве
        transactions = load_transactions("data/operations.json")
        executed_count = sum(
            1
            for item in transactions
            if str(item.get("state", "")).upper() in ALLOWED_STATUSES and item["state"] == "EXECUTED"
        )
        self.assertIn(f"Всего банковских операций в выборке: {executed_count}", printed_text)


if __name__ == "__main__":
    unittest.main()
