import logging

# gets the right log settings
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# format that will be printed in the log file
formatter = logging.Formatter('s:%(levelname)s:%(message)s:%(asctime)s')

# log file name and sets the format defined by formatter
file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

# stream handler to show results in the terminal
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# DEBUG: Detailed information, related to treating problems

# INFO: Confirmation that things are working correctly

# WARNING: Something unexpected happened, or indicates some problem 
# might happen, the software still works correctly (default value for logging)

# ERROR: The software has not been able to perform some function

# CRITICAL: A serious errror, the software might be unable to continue to run

# logging is a different form of printing


def add(a, b):
    return a + b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

def sub(a, b):
    return a-b


n1, n2 = 2, 3
addRes = add(n1, n2)


# logs with warning. Warning
# is the default log status, although it can be changed
# through the use of the command below 

# logging.basicConfig(level=logging.DEBUG)
logger.debug(f'Add: {n1} + {n2} = {addRes}')

# will log to a file, the format part establishes more information
# to the log file


n1, n2 = 5, 2
subRes = sub(n1, n2)

logger.debug(f'Sub: {n1} + {n2} = {subRes}')