import logging

def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    default_handler = logging.StreamHandler()
    default_handler.setFormatter(
        logging.Formatter("[%(asctime)s] [%(process)d] [%(levelname)s] [%(module)s] %(message)s")
    )
    logger.addHandler(default_handler)

    return logger