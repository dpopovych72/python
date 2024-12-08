"""
This is an app that will help you create a password
"""


# checks if password has lower and upper letters 
try:
    def ups_lows(word):   
        uppers = []
        lowers = []
        
        for char in word :
            #print(char)
            if char.isupper() == True :
                uppers.append(char)
            if char.islower()==True:
                lowers.append(char)
       # print("They are up: " ,uppers)
        #print("They are low: ", lowers)
        
        return uppers , lowers
        
    # checks if the password has any numbers
    def any_nums(new_word):
        count= 0 
        for char in new_word :
           # print(char.isdigit())
            if char.isdigit()==True:
                count+=1
        return count
        
    # checks if the password has any special characters 
    def any_specials(word_2):
        count_specials = 0
        specials = "!@#$%&*"
        for char in specials :
            #print(char in word_2)
            if char in word_2:
                count_specials +=1
        return count_specials 
        
    # runs all of the process , also uses all of the listed above functions       
    def main():
        password = ""
        while True :
            if len(password) >= 8 :
                if len(password) < 20:
                    uppers , lowers = ups_lows(password)
                    if len(uppers)>0:
                        if len(lowers)>0:
                            count = any_nums(password)
                            if count > 0:
                                count_specials = any_specials(password)
                                if count_specials > 0:
                                    break
            password = input("Please enter a password: ")
        while True :
            confirm_password = input("Please confirm your password : ")
            if confirm_password == password :
                print("Great , your password is all set ")
                break
except: 
    print("Sorry , something went wrong ")


    #print("this is your ",password)
    
    
    
print("Please create a password that meets all of the listed expectations  ")
print("The length of the password should be less than 20 but more or equal to 8")
print("It must include 1 or more capital, lower letter and 1 or more digit ")
print("It must also include any special character from this choice : !@#$%&*")
main()

