import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=r".//Logs//autom.log",
#                          format = "%(asctime)s:%(levelname)s:%(message)s",
#                          datefmt= "%Y-%m-%d %H:%M:%S")
#
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger


import logging
class LogGen():
    @staticmethod
    def loggen():
    # getLogger() method takes the test case name as input
        logger = logging.getLogger(__name__)
    # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler(r'.\\Logs\\autom.log')
    # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")

        fileHandler.setFormatter(formatter)


    # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)
    # setting the logger level
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)
        return logger
