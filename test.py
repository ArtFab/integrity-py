from integrity import Integrity
import traceback

def fail(x):
    print("-------- FAIL --------")
    if(type(x) == str):
        print(x)
    else:
        print("Exception occured")
        print(x.__class__)
        print(traceback.format_exc())

# Examples which should succeed

try:
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
    Integrity.checkIsValidNumber(1);
    Integrity.checkIsValidNumber(1.1)
    Integrity.checkIsValidNumber(0);
    Integrity.checkIsValidNumber(0)
    Integrity.checkIsValidNumber(-0)


    print("PASSED")

except Exception as e:
    fail(e)

# examples were we expect an excepiton to be raised...

try:
    Integrity.checkStringNotNoneOrEmpty("")
    fail("empty string")
except:
    pass

try:
    Integrity.checkStringNotNoneOrEmpty(None)
    fail("None string")
except:
    pass

try:
    Integrity.checkStringNotNoneOrEmpty(one)
    fail("one is not a string")
except:
    pass

try:
    Integrity.checkIsValidNumber(float("nan"))
    fail("nan is not a valid number")
except:
    pass

try:
    Integrity.checkIsValidNumber(float("Infinity"))
    fail("Infinity is not a valid number")
except:
    pass

try:
    Integrity.checkIsValidNumber(float("-Infinity"))
    fail("Infinity is not a valid number")
except:
    pass

