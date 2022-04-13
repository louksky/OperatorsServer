import time


class local_timer:
    """
    Class designed to provide sampling capabilities-
    of the time the function is performed
    """
    BASE_MILESECONDS = 1000
    def __init__(self):
        self.first = self.eval_time()
        self.second = None
    def reset(self):
        self.first = self.eval_time()
    def get_current_time(self):
        self.second = self.eval_time()
        time_taken = self.second - self.first
        return f'{time_taken} milliseconds'
    
    def eval_time(self):
        return int(round(time.time() * self.BASE_MILESECONDS))

#List of possible strings
SERVER_ON = 'Server status: on'
UNDEFINED_FORMULA = 'Illegal expression'
#List of possible system error
GENERAL_ERROR = 1000, 'General error: formula is not fit our api roles'
TYPE_ERROR = 1001, 'Type error: formula has a invalid syntax types of values'
SYNTAX_ERROR = 1002, 'Syntax error: formula has a invalid syntax types of operator'
KEY_ERROR = 1004, 'Key error: missing formula key'
BAD_REQ_ERROR = 1005, 'Bad request error: USE allowed methods'
EMPTY_OP_LIST = 1006, 'No operators are registered'
TWICE_OPERATOR_ERROR = 1007, 'Register operator twice is not allowed'
TWICE_SIGN_ERROR = 1008, 'Register operator with same sign is not allowed'
BAD_OPERATOR_SYNTAX = 1009, 'Syntax operator ERROR operator need to be str(string)'
NO_OPERATOR_CLASS_FOUND = 1010, 'Dev team no.1010'