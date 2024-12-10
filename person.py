"""
Your task is to design and implement a class in a programming language. This class will represent a person and hold personal data.
"""

class Person :
    def __init__(self, name, adress , age , phone):
        self.__name = name
        self.__adress = adress
        self.__age = age
        self.__phone = phone
      
    # This getter will show all of the stored data   
    def get_info(self):
        return (f"His name is {self.__name}\n"
                f"he lives on {self.__adress}\n"
                f"he is {self.__age} years old\n"
                f"and his phone number is :{self.__phone}")
      
    # Those get and set method will manage all of the data separately     
    def get_name(self):
        return self.__name
        
    def get_adress(self):
        return self.adress
        
    def get_age(self):
        return self.__age
        
    def get_phone(self):
        return self.__phone
        
    def set_name(self):
        return self.__name
        
    def set_adress(self):
        return self.adress
        
    def set_age(self):
        return self.__age
        
    def set_phone(self):
        return self.__phone
        
    
# Created 3 objects of the Person class  

big_Georgie = Person("George","Coconut 3400","46","5557772299")
little_Benny = Person("Benny","Chocolate 2560","9","1234567890")
uncle_john = Person("John","Milkyway 1300","37","7728819630")
print(big_Georgie.get_info())
print()
print(little_Benny.get_info())
print()
print(uncle_john.get_info())




