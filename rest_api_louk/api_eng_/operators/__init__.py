from api_eng_ import common
from api_eng_.operators.base_register import RegisteredOperators

# HERE add import
from .plus import *
from .multy import *
from .substruct import *
from .modulo import *

class RegisteredOperatorsEngine(RegisteredOperators):
    """
    HERE you must register classes in use
    """         
    def __init__(self):
        self.register(Plus())
        self.register(Multy())
        self.register(Moudulo())
        self.register(Substruct())

    def calculate(self):
        if not self.op_list:
            return common.EMPTY_OP_LIST
        

