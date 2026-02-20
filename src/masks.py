import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card):
    """
    Формирует маску номера банковской карты из 16 цифр.
    Параметры:
    card (str) - номер карты в виде строки из 16 цифр
    Возвращает:
    str - отформатированную маску номера карты
    Исключения:
    ValueError - если длина карты не 16 символов или присутствуют нечисловые символы
    """
    if not card.isdigit():
        error_msg_numbers = f"Карта должна содержать только числа"
        logger.error(error_msg_numbers)
        raise ValueError(error_msg_numbers)
    if len(card) != 16:
        error_msg_sixteen_digits = f"Карта должна содержать только 16 цифр, получено: {len(card)}"
        logger.error(error_msg_sixteen_digits)
        raise ValueError(error_msg_sixteen_digits)
    mask = f"{card[:4]} {card[4:6]}** **** {card[-4:]}"
    return mask


def get_mask_account(card):
    """
    Формирует маску счета из 20 цифр.
    Параметры:
    card (str) - номер счета в виде строки из 20 цифр
    Возвращает:
    str - отформатированную маску счета
    Исключения:
    ValueError - если длина счета не 20 символов или присутствуют нечисловые символы
    """
    if not card.isdigit():
        error_msg_numbers = f"Счет должен содержать только числа"
        logger.error(error_msg_numbers)
        raise ValueError(error_msg_numbers)
    if len(card) != 20:
        error_msg_twenty_digits = f"Счет должен содержать только 20 цифр, получено: {len(card)}"
        logger.error(error_msg_twenty_digits)
        raise ValueError(error_msg_twenty_digits)
    mask = f"**{card[-4:]}"
    return mask


try:
    raise Exception("Тестовая ошибка")
except Exception as e:
    logging.error("Произошла ошибка: %s", e)
