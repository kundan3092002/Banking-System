#Banking system 

def check_balance():
    print(f"Your balance is {balance}")
def deposit():
    amount = float(input("Enter your deposit amount =>  "))
    if amount < 0:
        print("not a vaild")
    else: 
        return 0
        return amount
def withdrawal():

    amount = float(input("Enter your withdrawal amount =>  "))
    if amount < 0:
        print("not a vaild amount!")
    else: 
        return amount

balance = 0
running_balance = True

while running_balance == True:
    print("Welcome to Banking system")
    print("1. check balance ")
    print("2. deposit ")
    print("3. withdrawal ")
    print("4. Exit")
    
    choice = input("Enter your choice(1 to 4)  => ")
    
    if choice == '1':
        check_balance()
    elif choice == '2':
        balance += deposit()
        print(f"your balance is {balance}")
    elif choice == '3':
       balance -= withdrawal()
    elif choice == '4':
        running_balance = False
        print("Thank you for using Banking system ")
    else:
        print("not a vaild input")
       

