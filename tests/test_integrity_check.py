import unittest
from integrity_check import Integrity

class Test_test_a(unittest.TestCase):
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
            #Integrity.checkIsFunction(fail)

    def test_checks_which_should_raise_an_error(self):
        zero = 0
        nan = float('nan')
        one = 1
        two = 2
        self.assertRaises(TypeError, Integrity.check, 1)
        self.assertRaises(TypeError, Integrity.check, None)
        self.assertRaises(TypeError, Integrity.check, "1")
        self.assertRaises(ValueError, Integrity.check, False)
        self.assertRaises(ValueError, Integrity.checkNotNone, None)
        self.assertRaises(TypeError, Integrity.checkIsBool, 0)
        self.assertRaises(TypeError, Integrity.checkIsBool, nan)
        self.assertRaises(TypeError, Integrity.checkIsBool, "")
        self.assertRaises(TypeError, Integrity.checkIsBool, " ")
        self.assertRaises(TypeError, Integrity.checkIsBool, one)
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




if __name__ == '__main__':
    unittest.main()
