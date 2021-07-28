import logging

# Set Defualt Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')

# Set My Logger

my_logger = logging.getLogger('MY_FLASK_LOG')
my_logger.setLevel(logging.DEBUG)
#   콘솔에 log 남기기
stream_log = logging.StreamHandler()
stream_log.setFormatter(formatter)
my_logger.addHandler(stream_log)
# Log disabled
# my_logger.disabled = True


