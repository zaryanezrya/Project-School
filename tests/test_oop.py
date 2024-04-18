import unittest


class A:
    def print_class_info():
        print("Hello from class A")
    
    def print_object_info(self):
        print("Hello from object A")

class B:
    def __init__(self, val):
        self.value = val

    def get_value(self):
        return self.value
    

    def set_value(self, new_value):
        self.value = new_value

class Clicker:
    def __init__(self):
        self.value = 0

    def click(self):
        self.value = self.value + 1
    
    def reset(self):
        self.value = 0
    
    def get_value(self):
        return self.value

    

class TestOOP(unittest.TestCase):
    def test_example_1(self):
        A.print_class_info()

        ex1 = A()
        ex1.print_object_info()

    def test_example_2(self):
        ex1 = B("asdads")
        val = ex1.get_value()

        self.assertEqual(val, 'asdads')

        ex1.set_value("a")
        val = ex1.get_value()
        self.assertEqual(val, 'a')

    def test_clicker(self):
        c1 = Clicker()

        c2 = Clicker()
        val = c1.get_value()
        c1.click()
        c1.click()
        c1.click()
        c2.click()
        c2.click()
        val = c1.get_value()
        c1.reset()
        c2.click()
        val = c1.get_value()
        c1.click()
        c1.click()
        c2.click()
        val1 = c1.get_value()
        val2 = c2.get_value()
