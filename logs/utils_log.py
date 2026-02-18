import logging

logger = logging.getLogger(__name__)
# Создаем хендлер для вывода в файл
file_handler = logging.FileHandler('logs/utils.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


logger = logging.getLogger(__name__)
logging.basicConfig(filename='utils.log', filemode='w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')


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