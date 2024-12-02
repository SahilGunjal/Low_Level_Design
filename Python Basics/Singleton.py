import threading
import time
from threading import Thread


class SingletonExample(Thread):
    __loggerInstance = None
    # tempVar = "Hello"
    lock = threading.Lock()

    @staticmethod
    def getLoggerInstance():
        if SingletonExample.__loggerInstance is None:
            with SingletonExample.lock:
                if SingletonExample.__loggerInstance is None:
                    time.sleep(2)
                    SingletonExample.__loggerInstance = SingletonExample()

        return SingletonExample.__loggerInstance


class createObj1(Thread):
    def run(self):
        loggerObj1 = SingletonExample.getLoggerInstance()
        print(loggerObj1)


class createObj2(Thread):
    def run(self):
        loggerObj2 = SingletonExample.getLoggerInstance()
        print(loggerObj2)


t1 = createObj1()
t2 = createObj2()

t1.start()
t2.start()

t1.join()
t2.join()


# -- Practice for static object
# obj1 = SingletonExample()
# obj2 = SingletonExample()
# print(obj1.tempVar)     # Hello
# obj1.tempVar = "hi"     # this will create a separate variable just for the obj1
# print(SingletonExample.tempVar) # Hello
# print(obj2.tempVar)     # Hello
# print(obj1.tempVar)     # Hi



