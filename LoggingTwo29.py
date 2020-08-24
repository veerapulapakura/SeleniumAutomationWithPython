import logging

logging.basicConfig(filename="C:\\Users\\User\\PycharmProjects\\pythonProjectSample\\SeleniumLogs\\logfile.log",
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")
