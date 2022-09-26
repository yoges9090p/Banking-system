import json
import pyinputplus
from mydatabase import Mybanking


class Customer:
    mydbobj = Mybanking('mybanking')
    def __init__(self):
        pass

    def account_open(self):
        print("You choose to open a new account!!!")
        name = input("Enter your first name: ") + " " + input("Enter your last name: ")
        email_address = pyinputplus.inputEmail(prompt="Enter your email address: ").lower()
        while Customer.mydbobj.ifalreadytaken('customer_email',f"\'{email_address}\'"):
            print("This email address is taken!!!")
            email_address = pyinputplus.inputEmail(prompt="Enter your email address: ").lower()

        phone_num = pyinputplus.inputNum(prompt="Enter your mobile number: ",min=1000000000,max=9999999999)
        while Customer.mydbobj.ifalreadytaken('customer_phone',f"\'{str(phone_num)}\'"):
            print("This phone number is already taken!!!")
            phone_num = pyinputplus.inputNum(prompt="Enter your mobile number: ")
        dob = input("Enter your dob: ")
        password = pyinputplus.inputPassword(prompt="Enter a password for your account: ")
        customer_id = Customer.mydbobj.currentcustomerid() + 1
        output_tup = tuple([customer_id,name,email_address,phone_num,dob,str(password),str(0)])
        Customer.mydbobj.tupleinserter(output_tup)

    def user_auth(self, extra_query):
        email_address = pyinputplus.inputEmail(prompt="Enter your registered email address: ")
        password = pyinputplus.inputPassword(prompt="Enter your password: ")
        response = Customer.mydbobj.currentbalance(extra_query,f"\'{email_address}\'",f"\'{password}\'")
        return response

    def update_balance(self,action):
        email_address = pyinputplus.inputEmail(prompt="Enter your registered email address: ")
        password = pyinputplus.inputPassword(prompt="Enter your password: ")
        current_balance = Customer.mydbobj.currentbalance('current_balance',f"\'{email_address}\'",f"\'{password}\'")
        current_user_id = Customer.mydbobj.currentbalance('customer_id',f"\'{email_address}\'",f"\'{password}\'")
        if current_balance is None:
            print("Your email and password doesn't match!!!")
        else:
            amount = pyinputplus.inputNum(prompt=f"Enter the amount you want to {action} :  ")
            if action =='deposit':
                new_balance = f"\'{current_balance + amount}\'"
                Customer.mydbobj.updatebalance(current_user_id,new_balance)
            elif action =='withdraw':
                if amount > current_balance:
                    print("Not enough money in your account!!!")
                else:
                    new_balance = f"\'{current_balance - amount}\'"
                    Customer.mydbobj.updatebalance(current_user_id,new_balance)



