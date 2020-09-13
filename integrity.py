
class Integrity:
    @staticmethod
    def check(condition, *msg):
        '''If condition is not true, then raises an exception, with default or optional message

        Args:
            condition (bool): The condition which must be true
            msg (any): Optional. See docstring for deferredStringBuilder

        Raises:
            TypeError: if condition is not a bool (including if it is None)
            ValueError: if condition is false
        '''
        if(condition is None):
            raise TypeError("Expected bool but was None");

        if(not isinstance(test, bool)):
            raise TypeError("Expected bool but was " + str(type(test)));

        if(not condition):
            text = Integrity.__getMessage("Integrity check failed", msg)
            raise ValueError(text)

    @staticmethod
    def checkNotNone(test, *msg):
        '''If test is exactly None then raises an exception with default or optional message

        Args:
            condition (bool): The condition which must be true
            msg (any): Optional. See docstring for deferredStringBuilder

        Raises:
            ValueError: if and only if test is exctly None
        '''
        if(test is None):
            text = Integrity.__getMessage("None encountered", msg)
            raise ValueError(text)

    @staticmethod
    def checkIsBool(test, *msg):
        if(not isinstance(test, bool)):
            text = Integrity.__getMessage(Integrity.__getTypeErrorDefaultString("bool", test), msg)
            raise TypeError(text)

    @staticmethod
    def checkIsBoolOrNone(test, *msg):
        if(test is not None):
            if(not isinstance(test, bool)):
                text = Integrity.__getMessage(Integrity.__getTypeErrorDefaultString("bool", test), msg)
                raise TypeError(text)

    @staticmethod
    def checkIsString(test, *msg):
        if(not isinstance(test, str)):
            text = Integrity.__getMessage(Integrity.__getTypeErrorDefaultString("string", test), msg)
            raise TypeError(text)

    @staticmethod
    def checkIsStringOrNone(test, *msg):
        if(test is not None):
            if(not isinstance(test, str)):
                text = Integrity.__getMessage(Integrity.__getTypeErrorDefaultString("string", test), msg)
                raise TypeError(text)

    @staticmethod
    def checkStringNotNoneOrEmpty(test, *msg):
        if(not isinstance(test, str)):
            text = Integrity.__getMessage(Integrity.__getTypeErrorDefaultString("string", test), msg)
            raise TypeError(text)
        if(test == ""):
            text = Integrity.__getMessage("Empty string", msg)
            raise ValueError(text)

    @staticmethod
    def checkIsValidNumber(test, *msg):
        if(isinstance(test, int)):
           return; # check for bool?

        if(not isinstance(test, int) and not isinstance(test, float)):
            text = Integrity.__getMessage(Integrity.__getTypeErrorDefaultString("string", test), msg)
            raise TypeError(text)
        if(test != test):
            text = Integrity.__getMessage("NaN", msg)
            raise ValueError(text)

        if(test != test):
            text = Integrity.__getMessage("NaN", msg)
            raise ValueError(text)
        positive_infnity = float('inf') 
        negative_infnity = float('-inf') 
        if(test == positive_infnity):
            text = Integrity.__getMessage("Infinity", msg)
            raise ValueError(text)
        if(test == negative_infnity):
            text = Integrity.__getMessage("-Infinity", msg)
            raise ValueError(text)



    @staticmethod
    def __getTypeErrorDefaultString(expectedTypeString, item):
        prettyValue = str(item)
        if(hasattr(item, "__class__")):
            prettyType = item.__class__.__name__
        else:
            prettyType = type(item)

        return "Expected " + expectedTypeString + " but was " + prettyType + ", value was '" + prettyValue + "'"

    @staticmethod
    def deferredStringBuilder(defaultMessage, *messageParts):
        return Integrity.__getMessage(defaultMessage, messageParts)

    @staticmethod
    def __getMessage(default, msg):

        if(msg is None):
            return default

        if(len(msg) == 0):
            return default

        s = "";
        for item in msg:
            pos = s.find("{}")
            if(pos != -1):
                s = s.replace("{}",  str(item), 1)
            else:
                if(s == ""):
                    s += str(item)
                else:
                    s += ", " + str(item)

        return s
