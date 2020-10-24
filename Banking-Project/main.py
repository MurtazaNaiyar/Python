__author__ = 'user'
import functions
import database
from os import system 
import cx_Oracle
from connection import con,cur

def main():
    try:
        database.make_all_tables()
    except:
        print('Test fail!!!')
    database.reset_withdrawals()
    choice = 1
    while choice != 0:
        system('cls')
        print("\n\n-----------Main Menu ------------- ")
        print("1. Sign Up (New Customer) ")
        print("2. Sign In (Existing Customer) ")
        print("3. Admin Sign In ")
        print("0. Close Application")

        try:
           choice = int(input())

        except:
           print("Invalid Choice")
           choice = 1
           continue

        if choice == 1:
           functions.sign_up();

        elif choice == 2:
           functions.sign_in();

        elif choice == 3:
           functions.admin_validate();

        elif choice == 0:
           print("Application Closed")

        else:
           print("Invalid Choice")
           
main()
