'''Define a class Person and its two child classes: Male and Female. All classes have a
method "getGender" which can print "Male" for Male class and "Female" for Female
class.'''

#Inheritance
#Method overriding

class Person:
    def getGender(self):
        print("Person")

class Male(Person):
    def getGender(self):
        print("Male")
        
class Female(Person):
    def getGender(self):
        print("Female")

person = Person()
male = Male()
female = Female()

person.getGender()
male.getGender()
female.getGender()