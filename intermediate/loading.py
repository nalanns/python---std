import logging


logging.basicConfig(level=logging.DEBUG)

# logging.info("Loading module initialized.")
# # This module is responsible for loading data or resources.
# logging.critical("This is a critical log message.")

logger = logging.getLogger("alo") 
# logger.info("Logger 'alo' initialized.")
# logger.warning("This is a warning log message.")
# logger.error("This is an error log message.")
# logger.debug("This is a debug log message.")
# # The above code sets up logging for the module, allowing for different levels of log messages.

logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("intermediate/loading.log")
handler.setLevel(logging.DEBUG)


formatter = logging.Formatter(' %(levelname)s - %(asctime)s : %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.debug("This is a debug log message with a specific level.")
logger.info("This is an info log message with a specific level.")

# logger.log(logging.ERROR, "This is an error log message with a specific level.")
# # The logging module is used to log messages at different severity levels.
# # The logger can be used to log messages that are specific to this module.

 
 