from datetime import datetime
import random

dataBaseUsers = {}


def register():

    print('*********REGISTER*********')

    firstName = input('What is your first name? \n')
    lastName = input('What is your last name? \n')
    password = input('Create a password. \n')

    accountNumber = generateAccountNumber()

    dataBaseUsers[accountNumber] = [firstName, lastName, password]

    print('==========================')
    print('Registration successful!')
    print(f'Your account number is {accountNumber}')
    print('Make sure you keep it safe!')
    print('==========================')
    login()
    

def login():
    
    print('**********LOG IN**********')

    userAccountNumber = int(input('Enter your account number: \n'))
    userPassword = input('Enter your password: \n')

    for accountNumber, userDetails in dataBaseUsers.items():
        if accountNumber == userAccountNumber:
            if userDetails[2] == userPassword:

                print('========================================')
                now = datetime.now()
                print("Now: ", now)
                print('You have successfully logged in.')
                bankOperations(userDetails)

    print('Invalid account number or password. Please try again!')
    login()

    
def bankOperations(user):
    print(f'Welcome, {user[0]} {user[1]}.')
    selectedOption = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Complaint (4) logout (5) Exit \n'))

    if selectedOption == 1:
        deposit()
    
    elif selectedOption == 2:
        withdrawal()

    elif selectedOption == 3:
        complaint()

    elif selectedOption == 4:
        login()

    elif selectedOption == 5:
        print('Thank you for banking with us!')
        exit()
        
    else:
        print('Invalid option selected. Please try again!')
        bankOperations(user)

    

def deposit():
    amountDeposited = int(input('How much would you like to deposit? \n'))
    print(f'You have deposited ${amountDeposited}')
    logout()

def withdrawal():
    int(input('How much would you like to withdraw? \n'))
    print('Please take your cash.')
    logout()

def complaint():
    input('What issue will you like to report? \n')
    print('Thank you for contacting us. We shall get back to you shortly!')
    logout()

def logout():
    option = int(input('Press (1) To return to the MAIN MENU (2) To exit \n'))
    
    if option == 1:
        init()

    elif option == 2:
        print('Thank you for banking with us!')
        exit()

    else:
        print('Invalid option selected. Please try again!')
        logout()



def generateAccountNumber():
    return random.randrange(1111111111,9999999999)


def init():
    print('**********MAIN MENU**********')
    print('Welcome to Zuri Bank')
    haveAccount = int(input('Do you have an account with us?  (1) Yes (2) No \n'))

    if haveAccount == 1:
        login()

    elif haveAccount == 2:
        register()

    else:
        print('Invalid option. Please try again!')
        init()
    
    

init()