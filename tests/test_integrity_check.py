import unittest
from integrity_check import Integrity

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

class Test_integrity_check(unittest.TestCase):
    def test_checks_which_should_pass(self):
            zero = 0
            nan = float('nan')
            one = 1
            two = 2
            Integrity.check(zero == zero)
            Integrity.check(one == one)
            Integrity.check(nan != nan) # nan never equals itself
            Integrity.checkIsBool(True)
            Integrity.checkIsBool(False)
            Integrity.checkIsBool(two == two)
            Integrity.checkIsString("")
            Integrity.checkIsString("a")
            Integrity.checkIsStringOrNone("")
            Integrity.checkIsStringOrNone("a")
            Integrity.checkStringNotNoneOrEmpty("a")
            Integrity.checkIsValidNumber(1)
            Integrity.checkIsValidNumber(1.1)
            Integrity.checkIsValidNumber(0)
            Integrity.checkIsValidNumber(0)
            Integrity.checkIsValidNumber(-0)
            Integrity.checkIsValidNumberOrNone(None)
            Integrity.checkIsValidNumberOrNone(1)
            Integrity.checkIsValidNumberOrNone(1.1)
            Integrity.checkIsValidNumberOrNone(0)
            Integrity.checkIsValidNumberOrNone(0)
            Integrity.checkIsValidNumberOrNone(-0)
            Integrity.checkIsFunction(self.test_checks_which_should_pass)
            Integrity.checkIsFunctionOrNone(self.test_checks_which_should_pass)
            Integrity.checkIsFunctionOrNone(None)


            #Integrity.checkIsFunction(fail)

    def test_checks_which_should_raise_an_error(self):
        zero = 0
        nan = float('nan')
        one = 1
        two = 2

        self.assertRaises(ValueError, Integrity.fail)
        self.assertRaises(TypeError, Integrity.check, 1)
        self.assertRaises(TypeError, Integrity.check, NotImplemented)
        self.assertRaises(TypeError, Integrity.check, None)
        self.assertRaises(TypeError, Integrity.check, "1")
        self.assertRaises(ValueError, Integrity.check, False)
        self.assertRaises(ValueError, Integrity.checkNotNone, None)
        self.assertRaises(TypeError, Integrity.checkIsBool, NotImplemented)
        self.assertRaises(TypeError, Integrity.checkIsBool, 0)
        self.assertRaises(TypeError, Integrity.checkIsBool, nan)
        self.assertRaises(TypeError, Integrity.checkIsBool, "")
        self.assertRaises(TypeError, Integrity.checkIsBool, " ")
        self.assertRaises(TypeError, Integrity.checkIsBool, one)
        self.assertRaises(TypeError, Integrity.checkIsBoolOrNone, NotImplemented)
        self.assertRaises(TypeError, Integrity.checkIsBoolOrNone, 0)
        self.assertRaises(TypeError, Integrity.checkIsBoolOrNone, nan)
        self.assertRaises(TypeError, Integrity.checkIsBoolOrNone, "")
        self.assertRaises(TypeError, Integrity.checkIsBoolOrNone, " ")
        self.assertRaises(TypeError, Integrity.checkIsBoolOrNone, one)
        self.assertRaises(TypeError, Integrity.checkIsString, None)
        self.assertRaises(TypeError, Integrity.checkIsString, one)
        self.assertRaises(TypeError, Integrity.checkIsString, nan)
        self.assertRaises(TypeError, Integrity.checkIsString, one)
        self.assertRaises(TypeError, Integrity.checkIsString, one == one)
        self.assertRaises(TypeError, Integrity.checkIsStringOrNone, one)
        self.assertRaises(TypeError, Integrity.checkIsStringOrNone, nan)
        self.assertRaises(TypeError, Integrity.checkStringNotNoneOrEmpty, one)
        self.assertRaises(TypeError, Integrity.checkStringNotNoneOrEmpty, None)
        self.assertRaises(ValueError, Integrity.checkStringNotNoneOrEmpty, "")
        self.assertRaises(TypeError, Integrity.checkIsValidNumber, None)
        self.assertRaises(TypeError, Integrity.checkIsValidNumber, "")
        self.assertRaises(ValueError, Integrity.checkIsValidNumber, nan)
        self.assertRaises(TypeError, Integrity.checkIsValidNumber, True)
        self.assertRaises(TypeError, Integrity.checkIsValidNumber, False)
        self.assertRaises(TypeError, Integrity.checkIsValidNumber, one == one)
        self.assertRaises(TypeError, Integrity.checkIsValidNumber, one == two)
        self.assertRaises(ValueError, Integrity.checkIsValidNumber, float("Infinity"))
        self.assertRaises(ValueError, Integrity.checkIsValidNumber, float("-Infinity"))
        self.assertRaises(TypeError, Integrity.checkIsValidNumber, "0")
        self.assertRaises(TypeError, Integrity.checkIsValidNumberOrNone, "")
        self.assertRaises(ValueError, Integrity.checkIsValidNumberOrNone, nan)
        self.assertRaises(TypeError, Integrity.checkIsValidNumberOrNone, True)
        self.assertRaises(TypeError, Integrity.checkIsValidNumberOrNone, False)
        self.assertRaises(TypeError, Integrity.checkIsValidNumberOrNone, one == one)
        self.assertRaises(TypeError, Integrity.checkIsValidNumberOrNone, one == two)
        self.assertRaises(ValueError, Integrity.checkIsValidNumberOrNone, float("Infinity"))
        self.assertRaises(ValueError, Integrity.checkIsValidNumberOrNone, float("-Infinity"))
        self.assertRaises(TypeError, Integrity.checkIsValidNumberOrNone, "0")
        self.assertRaises(TypeError, Integrity.checkIsFunction, None)
        self.assertRaises(TypeError, Integrity.checkIsFunction, "0")
        self.assertRaises(TypeError, Integrity.checkIsFunction, True)
        self.assertRaises(TypeError, Integrity.checkIsFunction, False)
        self.assertRaises(TypeError, Integrity.checkIsFunction, "a")
        self.assertRaises(TypeError, Integrity.checkIsFunction, "")
        self.assertRaises(TypeError, Integrity.checkIsFunction, 0)
        self.assertRaises(TypeError, Integrity.checkIsFunctionOrNone, "0")
        self.assertRaises(TypeError, Integrity.checkIsFunctionOrNone, True)
        self.assertRaises(TypeError, Integrity.checkIsFunctionOrNone, False)
        self.assertRaises(TypeError, Integrity.checkIsFunctionOrNone, "a")
        self.assertRaises(TypeError, Integrity.checkIsFunctionOrNone, "")
        self.assertRaises(TypeError, Integrity.checkIsFunctionOrNone, 0)

    def test_message_building(self):

        one = 1
        strB = "b"
        boolT = True
        arr = [one, strB, boolT]
        dict1 = { 'x': one, 'y' : strB, 'z' : boolT }
        dict2 = { one: 'and only', 2 : strB }
        point1 = Point(20, 30)

        self.assertEquals("", Integrity.deferredStringBuilder(""))
        self.assertEquals("a", Integrity.deferredStringBuilder("a"))
        self.assertEquals("1, 'b', True", Integrity.deferredStringBuilder(one, strB, boolT))
        self.assertEquals("1, 'b', True, ''", Integrity.deferredStringBuilder(one, strB, boolT, ""))
        self.assertEquals("1bTrue", Integrity.deferredStringBuilder("{}{}{}", one, strB, boolT))
        self.assertEquals("[1, 'b', True]", Integrity.deferredStringBuilder(arr))
        self.assertEquals("{'x': 1, 'y': 'b', 'z': True}", Integrity.deferredStringBuilder(dict1))
        self.assertEquals("{1: 'and only', 2: 'b'}", Integrity.deferredStringBuilder(dict2))
        
        # in future might want a nice way of printing an object which has no nice string representaiton
        #self.assertEquals("{10, 20}", Integrity.deferredStringBuilder(point1))
        
    def test_exceptions_have_messsage_building(self):
        arr = [1, 2, 3]
        dict1 = { 'a': 'b' }

        self.assertEquals("abc", self.get_x_message(Integrity.fail, "abc"))
        self.assertEquals("abc", self.get_x_message(Integrity.check, False, "abc"))
        self.assertEquals("abc", self.get_x_message(Integrity.check, False, "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkNotNone, None, "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkIsBool, 1, "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkIsBoolOrNone, 1, "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkIsString, None, "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkIsStringOrNone, 1, "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkStringNotNoneOrEmpty, None, "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkIsValidNumber, "zxz", "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkIsValidNumberOrNone, "zxz", "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkIsFunction, "zxz", "{}{}{}", 'a', 'b', 'c'))
        self.assertEquals("abc", self.get_x_message(Integrity.checkIsFunctionOrNone, "zxz", "{}{}{}", 'a', 'b', 'c'))

        # test default messages...


        self.assertEquals("Integrity check failed", self.get_x_message_no_main_arg(Integrity.fail))
        self.assertEquals("Expected bool but was None", self.get_x_message(Integrity.check, None))
        self.assertEquals("Expected bool but was str, value was 'a'", self.get_x_message(Integrity.check, 'a'))
        self.assertEquals("Integrity check failed", self.get_x_message(Integrity.check, False))
        self.assertEquals("None encountered", self.get_x_message(Integrity.checkNotNone, None))
        self.assertEquals("Expected bool but was int, value was '1'", self.get_x_message(Integrity.checkIsBool, 1))
        self.assertEquals("Expected bool but was int, value was '0'", self.get_x_message(Integrity.checkIsBoolOrNone, 0))
        self.assertEquals("Expected string but was None", self.get_x_message(Integrity.checkIsString, None))
        self.assertEquals("Expected string but was NotImplementedType, value was 'NotImplemented'", self.get_x_message(Integrity.checkIsString, NotImplemented))
        self.assertEquals("Expected string but was int, value was '1'", self.get_x_message(Integrity.checkIsStringOrNone, 1))
        self.assertEquals("Expected string but was None", self.get_x_message(Integrity.checkStringNotNoneOrEmpty, None))
        self.assertEquals("Expected float or int but was str, value was 'zxz'", self.get_x_message(Integrity.checkIsValidNumber, "zxz"))
        self.assertEquals("Expected float or int but was str, value was 'zxz'", self.get_x_message(Integrity.checkIsValidNumberOrNone, "zxz"))
        self.assertEquals("Expected function but was str, value was 'zxz'", self.get_x_message(Integrity.checkIsFunction, "zxz"))
        self.assertEquals("Expected function but was str, value was 'zxz'", self.get_x_message(Integrity.checkIsFunctionOrNone, "zxz"))
        self.assertEquals("Expected function but was dict, value was '{'a': 'b'}'", self.get_x_message(Integrity.checkIsFunctionOrNone, dict1))

    def get_x_message(self, func, test,  *msgargs):

        try:
            func(test, *msgargs)
        except Exception as inst:
             return str(inst)

        self.assertTrue(false)
    
    def get_x_message_no_main_arg(self, func, *msgargs):

        try:
            func(*msgargs)
        except Exception as inst:
             return str(inst)

        self.assertTrue(false)

if __name__ == '__main__':
    unittest.main()
