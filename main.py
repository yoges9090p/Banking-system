import json
from customer import Customer
import pyinputplus
import time
import os
mycustomer = Customer()


while True:
    os.system('clear')
    print("Hello!!!, welcome to the Yogesh Bank.")
    print("""
    Press 1 for opening a new account
    Press 2 to check your account balance
    Press 3 to withdraw money from your account
    Press 4 to deposit money to your account
    Press 5 to exit
            """)
    response = pyinputplus.inputNum(prompt="Enter your response here: ", max=5, min=1)
    if response==1:
            mycustomer.account_open()
            print("Congrats, your account has been opened")
    elif response==2:
        respons = mycustomer.user_auth('current_balance')
        if respons == None:
            print("Your email and password doesn't  match!!!")
        else:
            print(f"Your current balance is {respons}")

    elif response==3:
        mycustomer.update_balance('withdraw')
    elif response==4:
        mycustomer.update_balance('deposit')
    elif response==5:
        break
    time.sleep(3)








