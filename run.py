
import string
# import  random 
import random
from tokenize import Name
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
         

