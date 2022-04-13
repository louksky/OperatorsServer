from .base import *


class Multy(Mathmatic_Operator):
    math_operator = '*'
    val1 = 0
    val2 = 0 
    # overriding abstract method
    def eval(self):
        # write here the equation calculation
        return self.val1 * self.val2
    # overriding abstract method
    def set(self, n, m):
        try:
            self.val1 = float(n)
            self.val2 = float(m) 
        except:
            raise TypeError('Plus working only for float str(+) float')

