
from ntpath import join
import string
# import  random 
import random
from tokenize import Name
from unicodedata import name
from user import User
from user import credentials


def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser

def save_user(user):
    user.delete-user()

def find_user(number):
    return User.find_by_number(number)

def display_users():
    return User.display_users()

def create_account(accountusername,accountname,accountpassword):
    newaccount =credentials(accountusername,accountname,accountpassword)
    return newaccount

def save_account(user):
    user.save_account()

def  delete_account(user):
  user.delete_account()

def find_account(number):
    return credentials.find_by_number(number)

def display_accounts():
    return credentials.display_accounts()

def main():
    while True:
        print("Welcome to password locker write SU or LG to start")
        print("SU"_or_"LG")
        option = input()
        if option == "SU":
          print("Create Account")
          print("_"10)
          print("Enter your First Name ..")
          firstname = input()
          print("Enter your Last Name..")
          lastname =input()
          print("Set your username..")
          username = input()
          print("Set your password..")
          userpassword = input()
          save_user(create_user(firstname,lastname,username,userpassword))
          print("Your account was created succesfully.These are ur account details")
          print("_"10)
          print("f*name:{firstname}{lastname} \nusername:{username} \npassword:{userpassword}")
          print("\nuse Login to your account with your details")
          print("\n \n")
          # for user in display_user
          # prnt("f*name{user.firstname}{user.lastname}....{username}")
     

        elif option == "LG":
            print("your username")
            loginusername = input()
            print("your password")
            loginpassword = input()
            if find_user(loginpassword):
                print("\n")
                print("you can create multiple accounts (AC) and also view them(VC)")
                print("-"60)
                print("AC" _or_"VC")
                choose = input()
                print("\n")
                if choose == "AC" :
                    print("Add credential Account")
                    print("-"25)
                    accountusername=loginusername
                    print("Account Name")
                    accountname = input()
                    print("\n")
                    print("Generate automatic password(G) or Create new password(C)")
                    decision = input
                    if decision =="G":
                        characters = string.ascii_letters .string_digits
                        accountpassword = "",join(choose(characters)for x in range(random.randint(6,16)))


