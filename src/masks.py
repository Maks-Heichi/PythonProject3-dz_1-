import logging


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
    # if not card.isdigit():
    # print('карта должна содержать только числа')
    if len(card) != 16:
        print("карта должна содержать 16 чисел")
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
    # if not card.isdigit():
    # print('карта должна содержать только числа')
    if len(card) != 20:
        print("карта должна содержать 20 чисел")
    mask = f"**{card[-4:]}"
    return mask


logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def log_execution(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function {func.__name__} executed successfully.")
            return result
        except Exception as e:
            logger.error(f"Function {func.__name__} failed with error: {e}")
            raise

    return wrapper


@log_execution
def successful_function():
    return "Success!"


@log_execution
def error_function():
    raise ValueError("An error occurred!")


successful_function()

try:
    error_function()
except Exception:
    pass
