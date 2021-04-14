import random

bankUsers = {7245573145: ['Wale Tunde', 'shof@wale.com', '123456789', 0]}


def init():
        validSelections = False
        while validSelections == False:
                try:
                        accountExists = int(input('''Do you have an account with us?
1. Yes

2. No

3. Exit 
\n'''))

                        if accountExists == 1:
                                validSelections = True
                                login()
                        elif accountExists ==2:
                                validSelections = True
                                registerUser()
                        elif accountExists ==3:
                                validSelections = True
                        else:
                                print("You have made an invalid selection")
                except ValueError:
                        print("Invalid selection. Please choose 1, 2 or 3 as adviced")




def registerUser():
        print("Welcome to the registration page")
        firstName = input("Please enter your first name: \n")
        lastName = input("Please enter your last name :  \n")
        email = input("What is your email address?  \n") 
        password = input("Please enter your password \n") 
        fullname = firstName +" "+lastName
        accountBalance = 0
        accountno = generateAccountNo()
        bankUsers[accountno] = [fullname,email,password, accountBalance]
        print ("Your registration has been completed.")
        print ("Please Login to your account")
        print(bankUsers)
        login()


def generateAccountNo():
        accountNo = random.randrange(1111111111,9999999999)
        print (f"Your account number is {accountNo}")
        print("Please keep it protected and secured at all times")
        return accountNo


def login():
        print("Welcome to the Login page")
        userAccount = int(input("Please enter your Account Number: \n"))
        for accountNo, accountDetails in bankUsers.items():
                if accountNo == userAccount:
                    userPassword = input("Please enter your Account Password: \n")
                    if accountDetails[2] == userPassword:
                        print(f"Welcome {accountDetails [0]}")
                        print(f"You logged in at exactly time on date. Account operations is next")
                        accountOperations(accountDetails)
                    else:
                        print("Your password is incorrect. Please try again")
                else:
                    print("You entered an incorrect Account Number")


def accountOperations(accountDetails):
    selectedOperation = False
    while selectedOperation == False:
        print('''These are the available options:
        1. Balance Enquiries
        2. Withdrawal
        3. Cash Deposit
        4. Complaint
        5. Exit''')
        try:
            selectedOption = int(input('Please select an option: \n'))
            if selectedOption == 1:
                selectedOperation = True
                balance_enquiries(accountDetails)
            elif selectedOption == 2:
                selectedOperation = True
                withdrawal(accountDetails)
            elif selectedOption == 3:
                selectedOperation = True
                deposit(accountDetails)
            elif selectedOption == 4:
                selectedOperation = True
                complaint()
            elif selectedOption == 5:
                break
            else:
                print("Your current selection is invalid")
                
        except ValueError:
                print("Your current selection is invalid")


def balance_enquiries(accountDetails):
    # for accountNo, accountDetails in bankUsers.items():
        print(f"Your current balance is {accountDetails [3]}")
        attemptAnotherTransaction()


def withdrawal(accountDetails):
    valid_withdrawal = False
    while valid_withdrawal == False:
        try:
                withdraw_amount = int(input('How much do you want to withdraw? \n'))
                # for accountNo, accountDetails in bankUsers.items():
                if withdraw_amount > accountDetails[3]:
                        print("Insufficient funds. Please try a lesser amount")
                else:
                        valid_withdrawal = True
                        accountDetails[3]-= withdraw_amount
                        print(f"Here is your {withdraw_amount}")
                        print("Please take your cash")
                        attemptAnotherTransaction()
        except ValueError:
            print("Invalid amount input please try again")


def deposit(accountDetails):
    valid_deposit = False
    while valid_deposit == False:
        try:
                deposit_amount = int(input('How much do you want to deposit? \n'))
            # for accountNo, accountDetails in bankUsers.items():
                if deposit_amount > 0:
                    valid_deposit = True
                    accountDetails[3]+= deposit_amount
                    print(f"You have successfully added {deposit_amount} to your account")
                    print(f"Your total balance is now {accountDetails[3]}")
                    attemptAnotherTransaction()
                else:
                    print("You can not deposit zero or negative figures into your account")
        except ValueError:
            print("Invalid deposit amount input please try again")


def complaint():
    message = input('What issue will you like to report? \n')
    print('Your complaint has been logged. Thank you for contacting us')
    attemptAnotherTransaction()

def attemptAnotherTransaction():
    newTxnAttempt = False
    while newTxnAttempt  == False:
        try:
            anotherAttempt = int(input('''Do you want to do another transaction?
            1. Yes

            2. No
            \n'''))
            if anotherAttempt == 1:
                newTxnAttempt = True
                login()
            elif anotherAttempt ==2:
                print("Thank you for banking with us.")
                break
            else:
                print("You have made an invalid selection")
        except ValueError:
                    print("Invalid selection. Please choose 1, 2 as adviced")


# to start our ATM application
init()
