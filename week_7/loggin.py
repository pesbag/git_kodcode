
import logging
from logging import getLogger
from string import Formatter
# 5
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')
logger5 = logging.getLogger(__name__)

logger5.info('Application started')
# 6
logging.basicConfig(level=logging.INFO,
                     format='%(asctime)s | %(levelname)s | %(message)s')
loger6 = logging.getLogger("loggin.py")

def process_payment(user_id, amount):
    # print(f'Starting payment for user {user_id}')
    logging.info('Starting payment for user %s',user_id)
    if amount <= 0:
        # print('ERROR: Invalid amount')
        logging.error('ERROR: Invalid amount %s',amount)
        return
    if amount > 10000:
        logging.warning('WARNING: Large transaction %s',amount)
        # print('WARNING: Large transaction')
    # print(f'Payment of {amount} completed for user {user_id}')
    logging.info('Payment of %s completed for user %s',amount,user_id)
# process_payment(1234,100)
# 7
logger6=logging.getLogger('payment')
logger6.setLevel(logging.INFO)
file_handler=logging.FileHandler(
    'app.log', encoding='utf-8')
formatter=logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
file_handler.setFormatter(formatter)
logger6.addHandler(file_handler)
def divide(a,b):
    logger6.info("start the function")
    try:
        logger6.warning("check if the division is valid")
        return a/b
    except ZeroDivisionError:
        print("cannot divide by zero")
        logger6.exception("the process was ended successfully")
# divide(2,1)
# 8
logger8=logging.getLogger('ex8')
logger8.setLevel(logging.INFO)
file_handler=logging.FileHandler('ex8.log',encoding="utf-8")
formatter=logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
file_handler.setFormatter(formatter)
logger8.addHandler(file_handler)

def read_config(filepath):
    logger8.debug('the file path is %(file path)s',filepath)
    try:
        with open(filepath) as f:
            data = f.read()
        logger8.info("success")
        return data
    except FileNotFoundError:
        logger8.exception("Error: an exception")
        return None
read_config("result.txt")

# 9
def write_structured_log(message,module,level,**extra):
    pass
# 10 a
# logger.info('done')
# חסר אינפורמציה אמיתית על השלב שבו השתמשנו בלוגר. האינפורמציה כרגע לא נותנת לנו מידע שאפשר ללמוד ממנו
# 10 b
# logger.error('failed')
# באופן דומה לסעיף הקודם הלוגר פה גם לא נותן לנו מידע שניתן להסיק ממנו מסקנות על תהליך שנכשל לנו. רק מודפס נכשל ולא כתוב למה או איך וכו'
# 10 c
# logger.info('user=%s', user_id)
# מה שטוב בלוגר הזה זה שהוא נותן לנו את הזהות של המשתמש אבל עדיין חסרה פה אינפורמציה שניתן להסיק ממנה מידע ולעבוד עם התוצאות שלה למשל באיזה שלב אנחנו ומה התבצע

# 11
#warning
#error
#worning
#worning
#info
#error

# 12
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def register_user(email, password, age):
    logger.debug('register enterd: %(email)s %(password)s %(age)s',email,bool(password),age)
    if age < 18:
        logger.error('Error the age %s is too low',age)
        return
    logger.info('ok email=%s password=%s', email, bool(password))
    logger.info('The process done')
# 13
# logger13=logging.getLogger('logging_setup.py')
def get_logger(name):
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter=logging.Formatter('%(asctime)s | %(name)s | %(message)s')
    file_handler=logging.FileHandler('file.log',encoding='utf-8')
    file_handler.setFormatter(formatter)
    stream_handler=logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
    return logger
def add(a,b):
    lg=get_logger("first modul")
    lg.info("enter to add at first modul")
    return a+b
def sub(a,b):
    lg=get_logger("second modul")
    lg.info("enter to add at second modul")
    return a-b
# add(2,2)
# sub(7,2)
# 14
def process_request(request_id,user_id,action):
    pass

# logger_s=logging.getLogger('aaa')
# formatter=logging.Formatter('%(asctime)s | %(levelname)s | %(name)s')
# stream_handler=logging.StreamHandler()

