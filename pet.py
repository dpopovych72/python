"""
Creating a class named pet , it's original types is set to DOG 
"""

class Pet :
    
    # setting 2 values for class Pet
    pet_type = "Dog"
    vet_name = "PetSOS"
    
    # there must be an init function each time after creating class
    def __init__(self,owner_first_name,owner_last_name,pet_id,pet_name):
        self.__owner_first_name=owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id=pet_id
        self.__pet_name=pet_name
      
    # gettters and setters for all properties     
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def set_owner_first_name(self,value):
        self.__owner_first_name = value
        
    def get_owner_last_name(self):
        return self.__owner_last_name
        
    def set_owner_last_name(self,value):
        self.__owner_last_name=value
        
    def get_pet_id(self):
        return self.__pet_id
        
    def set_pet_id(self,value):
        self.__pet_id=value
        
    def get_pet_name(self):
        return self.__pet_name
        
    def set_pet_name(self,value):
        self.__pet_name=value
        
    # displays all properties for requested pet     
    def display_pet_info(self):
        print(f"The ID : {self.__pet_id}")
        print(f"The name of a pet: {self.__pet_name}")
        print(f"The full name of the owner: {self.__owner_first_name} {self.__owner_last_name}")

# checks if particular object has provided attributes         
def check_property(val,name):
    return hasattr(val,name)
    
        
happy_pet=Pet("John","Snow","123456","Fluffy")
sad_pet =Pet("Rick","Grimes","555555","Donny")
angry_pet =Pet("John","Winchester","666666","Luceus") 

happy_pet.display_pet_info()
sad_pet.display_pet_info()
angry_pet.display_pet_info()
print(check_property(happy_pet,"set_pet_name"))
print(check_property(sad_pet,"get_pet"))
# Renaming sad_pet as Franko 
sad_pet.set_pet_name("Franko")
sad_pet.display_pet_info()

