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
    #if not card.isdigit():
        #print('карта должна содержать только числа')
    if len(card) != 16:
        print('карта должна содержать 16 чисел')
    mask = f'{card[:4]} {card[4:6]}** **** {card[-4:]}'
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
    #if not card.isdigit():
        #print('карта должна содержать только числа')
    if len(card) != 20:
        print('карта должна содержать 20 чисел')
    mask = f'**{card[-4:]}'
    return mask


logger = logging.getLogger(__name__)
# Создаем хендлер для вывода в файл
file_handler = logging.FileHandler('logs/masks.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


logger = logging.getLogger(__name__)
logging.basicConfig(filename='masks.log', filemode='w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')