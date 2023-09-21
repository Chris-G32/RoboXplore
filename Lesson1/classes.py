class Person:
    #Class variable
    NUMBER_OF_PEOPLE=0

    #self is a python convention used to reference the object itself
    def __init__(self,name,age):
        #Instance variables
        self.name=name
        self.age=age
        Person.NUMBER_OF_PEOPLE+=1

    def print(self):
        print(f"Name: {self.name}, Age: {self.age}")

    #Remove from the count of people
    def __del__(self):
        Person.NUMBER_OF_PEOPLE-=1

#This is an instance of the class person
person=Person("Chris",20)

person.print()
person.alphabetical_order()