class Bank_Account:
    print("WELCOME TO KK BANK")

    def __init__(self):
        self.amount = 0

    def login(self, ):
        self.__name = input("Enter name:")
        self.__password = input("Enter password:")
        print("Welcome", self.__name, "What do you wish to do?")

    def deposition(self, Amount):
        self.amount += Amount
        print("Amount successfully credited to your account\n""Final Account Balance=RS", self.amount)

    def withdraw(self, Amount):
        if self.amount - Amount >= 1000:
            self.amount -= Amount
            print("Amount successfully debited from your account\n""Final Account Balance=RS", self.amount)
        else:
            print("Sorry,Minimum balance should be at least RS.1000\n""Your Current Balance is RS", self.amount)

    def balance(self):
        print("Your balance is", self.amount)

b1 = Bank_Account()
b1.login()
for i in range(0, 20):
    print("1.DEPOSITION", "2.WITHDRAWAL", "3.CHECK BALANCE", "4.EXIT", sep="\n")
    choice = int(input("Enter the no you wish to choose:"))
    if choice == 1:
        Amount = float(input("Enter Amount to be Deposited in RS:"))
        b1.deposition(Amount)
    elif choice == 2:
        Amount = float(input("Enter Amount to be Withdrawn in RS:"))
        b1.withdraw(Amount)
    elif choice == 3:
        b1.balance()
    elif choice == 4:
        print("Thank you for using KK BANK")
        exit()
    else:
        print("Invalid value try again")

