
import string
# from random import 
import random
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
