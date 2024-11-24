"""
Topic: Basic python class and objects using constructor destructor private variable, class variable etc.

"""


# Class declaration -> (This is just a blueprint and does not allocate the memory
class Student:
    # This is class attribute and only one time memory gets allocated for this (as specific to Class and not to object)
    __collegeName = 'Rochester Institute of Technology'

    # Default Constructor -> it's being called automatically after each object creation
    def __init__(self, name):
        print(f'This is the default constructor {name}')

    # Parameterized constructor
    def __init__(self, name: str, studentId: str, address: str, phoneNumber: int):
        self.__name = name
        self.__studentId = studentId
        self.__address = address
        self.__phoneNumber = phoneNumber

    # Member function -
    # Note: As __collegeName is a class variable and not object we can call it using the `Student` Class directly
    def getStudentInformation(self):
        print(f' Student Name: {self.__name}\n Student ID: {self.__studentId}\n Student Address: '
              f'{self.__address}\n Student PhoneNumber: {self.__phoneNumber}\n Student College Name: {Student.__collegeName}')

    # Generally not needed unless we are dealing with opening and closing the files/ database connections, releasing
    # network sockets, Cleaning up temporary data or cache.
    # Python automatically handles this
    def __del__(self):
        print(f"Destructor called for Student {self.__name} with ID {self.__studentId}")


def main():
    # Object creation
    studentObj = Student("Sahil", "sg2736", "480 Clay Road, Rochester", 1234567890)

    # Python does not support the multiple constructors Python allows only one __init__ method per class
    # studentObj2 = Student("Mehul")  --- This will not work

    print("-------")
    # Calling the member function
    studentObj.getStudentInformation()

    print("-------")
    # Cannot access it as __name is a private variable
    # print("Trying to access the private data member from outside class: ", studentObj.__name)  --> This will throw error

    print("-------")
    # Cannot access it as __collegeName is a private class variable
    # print("Trying to access the private class variable from outside class: ", Student.__collegeName)

    print("----------")
    # Calling the destructor specifically (not needed as python invokes it automatically when program exits or
    # when the object goes out of scope.)
    del studentObj


# why need this? -> So, if we are running this as main file then only execute the main() and if we are including this
# as a module in another module/ .py file then it doesn't execute the main()
if __name__ == "__main__":
    main()