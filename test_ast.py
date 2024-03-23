import unittest

from abc import abstractmethod, ABC

class Evaluable(ABC):
    @abstractmethod
    def eval(self):
        ...

class BadEvaluable(Evaluable):
    def eval(self):
        return 1

class Constant(Evaluable):
    def __init__(self, val: int):
        self.value = val
    
    def eval(self):
        return self.value
        
class Add(Evaluable):
    def __init__(self, a: Evaluable, b: Evaluable):
        self.a = a
        self.b = b
    
    def eval(self):
        return self.a.eval() + self.b.eval()
    
    
class Mul(Evaluable):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def eval(self):
        return self.a.eval() * self.b.eval()


class TestAST(unittest.TestCase):
    def test_const(self):
        a = Constant(7)
        b = Constant(5)
        c = Constant(5)
        d = Constant(-2)
        print(a.eval(),b.eval(),c.eval(),d.eval())
    
    def test_add(self):
        a = Constant(7)
        b = Constant(5)
        c = Constant(5)
        d = Constant(-2)

        print(Add(a, b).eval())
        print(Add(c, d).eval())

    def test_mul(self):
        a = Constant(7)
        b = Constant(5)
        c = Constant(5)
        d = Constant(-2)
        print(Mul(a,b).eval())
        print(Mul(c,d).eval())

    def test_general(self):
        # (7+5) * (5-2)
        a = Constant(7)
        b = Constant(5)
        c = Constant(5)
        d = Constant(-2)

        res = Mul(Add(a, b), Add(c, d))
        print(res.eval())

    def test_bad_eval(self):
        be = BadEvaluable()
        be.eval()