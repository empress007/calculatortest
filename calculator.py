import sys
calDb = []
def createCalAcct() :
    userName = input("Create a username: ")
    userPassword = input("Create a password: ")
    if userName in calDb:
        print(f"{userName} has been tken.")
    else:
        calDb.append(userName)
        calDb.append(userPassword)
        print(f"Account Created Successfully")
        loginCalculator()
        
def value():
        val1 = float(input('enter the first value: '))
        val2 = float(input('enter the second value: '))
        return val1,val2      
def loginCalculator() : 
    userloginName = input("Enter your username: ")
    userloginPassword = input("Enter your password: ")
    if userloginName in calDb and userloginPassword in calDb:
        print("You are welcome")
        calculation()
    else:
        loginCalculator()


def calculation():
  while True:
    val = value()
    val1 = val[0]
    val2 = val[1] 
    userOption = input('Kindly choose an operator (+, -, /, *, **): ')
    if userOption == '+':
        print(val1 + val2)
    elif userOption == '-':
        print(val1 - val2)
    elif userOption =='/':
        print(val1 / val2)
    elif userOption == '*':
        print(val1 * val2)
    elif userOption == '**':
        print(val1 * val2)
    else:
        print("Please choose an operator from the user option")

while True:
    print(
        '''
        1.To create an account 
        2.To enter login details again
        3.To Exit
'''
    )
    choice = int(input('chose from the above option:(1,2,3)'))
    if choice == 1:
        createCalAcct()
    elif choice == 2:
        loginCalculator()
        # calculation()
    elif choice == 3:
         sys.exit('Exited')
    else:
        print('Invalid input')

