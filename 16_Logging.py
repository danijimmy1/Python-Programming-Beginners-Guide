# logging module in python gives Progress Reports of the code
# Purpose: Record Progress and problems ...
# Levels : Debug, Info, Warning, Error and Critical

import logging

# print(dir(logging))

# Create and Configure logger
# To fix this we need to uypdate basic config call and set level to DEBUG in line 10.

# Changing the format of the log
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
# To override the file every time change the file mode to 'w'.
logging.basicConfig(filename = "./16_Log.log",
	level = logging.DEBUG,
	format = LOG_FORMAT,
	filemode = 'w')
# Create logger object and call getLogger()
# Logger without the name is called root logger
logger = logging.getLogger()

# # Test the logger
# logger.info("Our Second Message")

# Get the level of the logger
#print(logger.level)
"""
What does this logger level means:

Level 			Numeric Value
------------------------------
NOTSET			0
DEBUG 			10
INFO 			20
WARNING 		30
ERROR 			40
CRITICAL 		50
------------------------------

Loggers only write the value greater than or equal to set level.
No value is written in the log file as the default value of root logger is 30.

"""

# Creating logger message with all five levels
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Jimmy.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")