import logging
from datetime import datetime
import random

def logger_object(name):
    time_stamp = datetime.now().strftime('%Y-%m-%d-%S')
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(f"create_logger.log")
    formatter = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(lineno)d : "
        "%(message)s - %(filename)s",
        datefmt='%m/%d/%Y %I:%M:%S %p')
    # %(module)s : %(funcName)s : %(threadName)s
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


names = ['Barnes', 'Kasparov', 'Topalov', 'Spasky', 'Capablanca', 'Tal','Fischer','Kramnik', 'Magnus', 'Morphy', 'Lasker', 'Anand', 'Karpov', 'Ivanchuk', 'Grischuk', 'Nakamura', 'Giri', 'Ding']
job = ['Good', 'Great', 'Fantastic']

def player_level(level, player):
    logs = logger_object(__name__)
    logs.debug(f"{player} is a {level} chess player.")


if __name__ == "__main__":
    player_level(random.choice(job), random.choice(names))