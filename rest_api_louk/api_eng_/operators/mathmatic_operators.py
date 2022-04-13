from abc import ABC, abstractmethod


class Mathmatic_Operator(ABC):
    """
       base class 
       Implement eval() & set()
    """
    math_operator: str = NotImplemented
    val1: any = NotImplemented
    val2: any = NotImplemented
    @abstractmethod
    def eval(self):
        """
        <name>   - <discription>    <(type)>
        op       - operator         (string)
        n        - dec value 1         (float/int/any)
        m        - dec value 2         (float/int/any)
        """
        pass
    @abstractmethod
    def set(self, n, m):
        """
        A function that uses one or more data and
        the identification mark of this class is operator
        """
        pass
 
"""
 Example class (not in use)
"""
class ExamplePlus(Mathmatic_Operator):
    math_operator = '+'
    val1 = 0
    val2 = 0 
    # overriding abstract method
    def eval(self):
        # write here the equation calculation
        return self.val1 + self.val2
    # overriding abstract method
    def set(self, n, m):
        try:
            self.val1 = float(n)
            self.val2 = float(m) 
        except:
            raise TypeError('Plus working only for float str(+) float')

