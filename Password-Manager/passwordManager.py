import sqlite3
import os
from cryptography.fernet import Fernet

file = open('Password-Manager/key.key', 'rb')
key = file.read()
file.close()

print(key)

con = sqlite3.connect("Password-Manager/accounts.db")
cur = con.cursor()

cur.execute('''   ''')

cur.execute('''CREATE TABLE IF NOT EXISTS accounts(
   ID INTEGER PRIMARY KEY,
   platform TEXT NOT NULL,
   email TEXT NOT NULL,
   password TEXT NOT NULL,
   username TEXT)''')

# TODO make a master password system

def action(userChoice):
   if userChoice == 1:
      viewAllAccounts()
   elif userChoice == 2:
      viewPasswordForAccount()
   elif userChoice == 3:
      newPlatform()
   
   return
   
def newPlatform():
   platform = input("Enter name of website/application you are adding an account for: ")
   email = input("Enter the email address you used for this account: ")
   password = input("Enter the password you used for this account: ")
   # Encrypt password before saving it
   fernet = Fernet(key)
   encPassword = ''
   encPassword = str(fernet.encrypt(password.encode())).replace("'","''")
   print(encPassword)
   strSQL = f"INSERT INTO accounts VALUES (NULL, '{platform}', '{email}', '{encPassword}', NULL)"
   cur.execute(strSQL)
   con.commit()

def viewAllAccounts():
   strSQL = "SELECT platform FROM accounts"
   cur.execute(strSQL)
   rows = cur.fetchall()

   for row in rows:
      print(row)

def viewPasswordForAccount():
   fernet = Fernet(key)
   platform = input("What platform do you want your password for?: ")
   strSQL = f"SELECT password FROM accounts WHERE platform = '{platform}'"
   cur.execute(strSQL)
   rows = cur.fetchall()
   for row in rows:
      print(f"The password for {platform} is: ")
      print(fernet.decrypt(eval(row[0])).decode())
      

# Welcome mesage
print("Hi, Welcome to Password Manager!")

userChoice = ''

while userChoice.lower() != 'q':

   validChoice = False
   while validChoice != True:
         # Menu system
         print("What would you like to do?")
         print("(1) View all platforms you have details saved for")
         print("(2) View Password for a certain platform")
         print("(3) Add new account")
         print("(q) Quit")
         userChoice = str(input(": "))
         if userChoice == '1' or userChoice == '2' or userChoice == '3' or userChoice == 'q':
            validChoice = True

   action(int(userChoice))
