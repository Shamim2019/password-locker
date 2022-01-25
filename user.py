import random
import string
from tkinter import SEL_FIRST
from tokenize import Number 


class user:

    userslist = []
def _init_(self,firstname,lastname,username,password):
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password


def save_user(self):
    user.userslist.append(self)

def delete_user(self):
    user.userslist.remove(self)

@classmethod  
def display_users(cls):
    return cls.userslist

@classmethod
def find_by_number(cls,number):
    for user in cls.userslist:
        if user.password == number:
            return user 


@classmethod
def user_exist(cls,number):
    for user in cls.userslist:
        if user.username == number:
           return True
           return False 


class credentials:
    accounts=[]
def _init_(self,accountusername,accountname,accountpassword):
    self.accountusername = accountusername
    self.accountname = accountname
    self.accountpassword = accountpassword


def save_account(self):
    credentials.accounts.append(self)

def delete_account(self):
    credentials.accounts.remove(self)

@classmethod 
def display_accounts(cls):
   for account in cls.accounts:
       return cls.accounts 

@classmethod
def find_by_number(cls,number):
   for account in cls.accounts:
       if account.accountusername == number:
           return account


