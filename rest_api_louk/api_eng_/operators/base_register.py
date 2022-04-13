from abc import ABC, abstractmethod
from api_eng_ import common
from api_eng_.operators.mathmatic_operators import Mathmatic_Operator


class BaseRegister(ABC):
    """
       base class 
       for manage operators
    """
    op_list: list(dict()) = NotImplemented

    @abstractmethod
    def register(self, operator_objcet: Mathmatic_Operator):
        """
        Function that will manage the registration of operators
        operator must to implement Mathmatic_Operator
        """
        pass

    @abstractmethod
    def eval(self, op: str, n, m):
        """
        Function that will manage the eval of registred operators
        operator must to be register to work
        """
        pass

    @abstractmethod
    def get_list(self):
        """
        Function that return list(string) of operators
        """
        pass


class RegisteredOperators(BaseRegister):
    op_list = list(dict())

    def register(self, operator_objcet: Mathmatic_Operator):
        if self.op_list:
            try:
                if next((x for x in self.op_list if x["op_object"] == operator_objcet), None):
                    raise Exception(common.TWICE_OPERATOR_ERROR)
                if next((x for x in self.op_list if x["operator"] == operator_objcet.math_operator), None):
                    raise Exception(common.TWICE_SIGN_ERROR)
                pass
            except Exception:
                raise Exception(common.BAD_OPERATOR_SYNTAX)
            # add new operator to list
            self.op_list.append({'operator': operator_objcet.math_operator, 'op_object': operator_objcet})
        else:
            if operator_objcet:
                self.op_list.append({'operator': operator_objcet.math_operator, 'op_object': operator_objcet})
            else:
                raise Exception(common.NO_OPERATOR_CLASS_FOUND)

    def eval(self, op: str, n, m):
        if self.op_list:
            operator_obj = next((x for x in self.op_list if x["operator"] == op), None)
            if operator_obj == None:  #
                raise Exception(common.SYNTAX_ERROR)
            else:
                try:
                    operator_obj['op_object'].set(n, m)
                    return operator_obj['op_object'].eval()
                except Exception as exr:
                    pass
        else:
            raise Exception(common.EMPTY_OP_LIST)

    def get_list(self):
        return ','.join(str(d['operator']) for d in self.op_list)
