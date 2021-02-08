import logging
import inspect


def customLogger(loglevel):
    # gets the name of the class where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # bydeafult log all msgs
    logger.setLevel(logging.DEBUG)

    c_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("{0}.log".format(logger_name), mode='w')
    c_handler.setLevel(loglevel)
    file_handler.setLevel(loglevel)

    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    c_handler.setFormatter(c_format)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(c_handler)

    return logger
