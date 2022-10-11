from random import randint
import re
import time
from datetime import date
from unicodedata import name
from unittest import TestCase
from xmlrpc.client import boolean
from tkinter import *


class User:
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    users_dict = {}

    def __init__(self, id_number=None, name=None):
        self.id_number = id_number
        self.name = name
        self.password = None
        self.email = None
        self.contact_number = None
        self.accounts = {}
        self.most_uses = []
        self.loans = []
        self.bills = []
        self.loan_month = []
        self.loan_status = False

    @staticmethod
    def login():
        username = input('Please enter your id number: ')
        if username in User.users_dict:
            user = User.users_dict.get(username)
            password = input('Please enter your password: ')
            if user.password == password:
                print("You have successfully loged in.\n")
                time.sleep(0.5)
                user.menu()
            else:
                print("\nYour password is not correct, Please try again.\n")
                User.login()
        else:
            print("User not found.")
            account = input('Do you have an account(y/n):?')
            if account == "y" or account == "Y" or account == "Yes" or account == "yes":
                User.login()
            elif account == "No" or account == "no" or account == "n" or account == "N":
                account_existence = input(
                    'Do you want to create an account(y/n): ')
                if account_existence == "y" or account_existence == "Y" or account_existence == "Yes" or account_existence == "yes":
                    User.register()
                    print("Now please login to your account")
                    User.login()
                else:
                    print("Hope to see you again.")
                    exit()

    @staticmethod
    def register():
        name = input('Please enter your name: ')
        id_number = input('Please enter your ID number: ')
        while id_number in User.users_dict:
            print("This ID already exists. please choose another one.")
            id_number = input('\nPlease enter your ID number: ')
        password = input('Please enter your password: ')
        email = input('Please enter your email: ')
        while bool(re.search(User.regex, email)) == False:
            if bool(re.search(User.regex, email)):
                break
            else:
                print("Invalid Email")
                email = input('Please enter a valid email: ')
        contact_number = input('Please enter your contact number: ')
        temp_user = User(id_number, name)
        temp_user.password = password
        temp_user.email = email
        temp_user.contact_number = contact_number
        User.users_dict[id_number] = temp_user
        print("You have been susseccfully registered. You can login now.\n")
        time.sleep(2)

    def menu(self):
        print("What do you want to do now?")
        time.sleep(1)
        print("1- Open new bank account")
        print("2- Account info")
        print("3- Manage account")
        print("4- Most used accounts")
        print("5- Transfer")
        print("6- Pay bills")
        print("7- Loan application")
        print("8- Closing account")
        print("9- Log out")
        action = input('Enter the number: \n')
        if action == '1':
            Account.create(self)
            self.menu()
        elif action == '2':
            Account.info(self)
            self.menu()
        elif action == '3':
            Account.manage(self)
            self.menu()
        elif action == '4':
            Account.most_used(self)
            self.menu()
        elif action == '5':
            Account.transfer(self)
            self.menu()
        elif action == '6':
            Account.pay_bill(self)
            self.menu()
        elif action == '7':
            Account.loan(self)
            self.menu()
        elif action == '8':
            Account.close(self)
            self.menu()
        elif action == '9':
            logout = input('Are you sure you want to logout?')
            if logout == "y" or logout == "Y" or logout == "Yes" or logout == "yes":
                print("Thanks for your visit")
                exit()
            elif logout == "No" or logout == "no" or logout == "n" or logout == "N":
                time.sleep(1)
                self.menu()
        else:
            time.sleep(1)
            print("Not valid answer. Please choose an item from menu.")
            time.sleep(1)
            self.menu()


class bill:
    bills_dict = {}

    def __init__(self, bill_id, bill_pay):
        self.bill_id = bill_id
        self.bill_pay = bill_pay
        self.key = (self.bill_id, self.bill_pay)
        self.amount = 0
        self.status = False
        bill.bills_dict[self.key] = self


class Account:
    all_accounts = {}
    issue_tracking_list = []

    def __init__(self, id):
        self.id = id
        self.name = None
        self.balance = 0
        self.password = None
        self.kind = None
        self.transaction = {}

    def create(user):
        flag = False
        account_id = ''.join(["{}".format(randint(0, 9))
                             for num in range(0, 10)])
        while account_id in Account.all_accounts:
            account_id = ''.join(["{}".format(randint(0, 9))
                                  for num in range(0, 10)])
        while flag == False:
            balance = input('How much money does your account have: ')
            try:
                balance = int(balance)
                flag = True
            except ValueError:
                print('Please enter an integer')
                time.sleep(0.5)
        password = input('Please enter a password for your acount: ')
        temp_account = Account(account_id)
        while flag == True:
            kind = input(
                'What kind of account is this(please enter the number): \n1- Current account \n2- Student account \n3- Children account \n')
            if kind == '1':
                temp_account.kind = 'Current account'
                flag = False
            elif kind == '2':
                temp_account.kind = 'Student account'
                flag = False
            elif kind == '3':
                temp_account.kind = 'Children account'
                flag = False
            else:
                print('Your answer is not valid. \nPlease try again')
                time.sleep(1)
        temp_account.name = account_id
        temp_account.balance = balance
        temp_account.password = password
        temp_account.kinf = kind
        temp_account.id = account_id
        Account.all_accounts[account_id] = temp_account
        user.accounts[temp_account.name] = temp_account
        time.sleep(1)
        print("Your account name is: " + str(account_id) + "\nYour account ID is: " + str(account_id) +
              "\nIts balance is: " + str(balance))
        account_name = input('Do you want to change the accounts name(y/n)? ')
        if account_name == "y" or account_name == "Y" or account_name == "Yes" or account_name == "yes":
            new_name = input('Enter the new name: ')
            while flag == False:
                if new_name in user.accounts:
                    print(
                        "You already have an account with this name. Try another name")
                    new_name = input('Enter the new name: ')
                else:
                    user.accounts[new_name] = user.accounts.get(
                        temp_account.name)
                    user.accounts.get(new_name).name = new_name
                    Account.all_accounts[temp_account.id] = user.accounts.get(
                        temp_account.name)
                    user.accounts.pop(temp_account.name)
                    Account.all_accounts.pop(temp_account.id)
                    flag = True
            print("Your account name is: " + str(new_name) + "\nYour account ID is: " + str(account_id) +
                  "\nIts balance is: " + str(balance))
        else:
            print("Your account name is: " + str(account_id) + "\nYour account ID is: " + str(account_id) +
                  "\nIts balance is: " + str(balance))
        time.sleep(1)
        input('Press ENTER to go back')

    def info(user):
        print("Name: " + user.name)
        time.sleep(0.5)
        print("ID number: " + user.id_number)
        time.sleep(0.5)
        print("Email: " + user.email)
        time.sleep(0.5)
        print("Contact number: " + user.contact_number)
        time.sleep(0.5)
        print("You have " + str(len(user.accounts)) + " accounts:")
        time.sleep(0.5)
        i = 1
        for key in user.accounts:
            temp_account = user.accounts.get(key)
            print(str(i) + "- "+"Account name: " + str(temp_account.name) + "\n   Account kind: " + str(temp_account.kind)+"\n   Account id: " + str(temp_account.id) +
                  "\n   balance: " + str(temp_account.balance) + "\n   Transactions:", end="\n               ")
            for keys in temp_account.transaction:
                print(temp_account.transaction[keys], end="\n               ")
            print(" ")
            time.sleep(0.5)
            i += 1
        time.sleep(1)
        input('Press ENTER to go back')

    def manage(user):
        print(
            "Manage: \n1- Creat new account \n2- View current account info \n3- Back to menu")
        time.sleep(0.5)
        action = input('Enter the action number:')
        if action == '1':
            Account.create(user)
            Account.manage(user)
        elif action == '2':
            Account.info(user)
            Account.manage(user)
        elif action == '3':
            user.menu()
        else:
            print("Your answer is not valid, please try again")
            Account.manage(user)

    def most_used(user):
        temp_account_id = input(
            'Enter the account id that you want to add to most used: \n(If finished enter done.)\n')
        # if temp_account_id in Account.all_accounts.keys(temp_account_id):
        if Account.all_accounts.keys():
            if temp_account_id in user.most_uses:
                print("It already exists is the list. Try another one.")
                time.sleep(1)
                Account.most_used(user)
            else:
                user.most_uses.append(temp_account_id)
                print("The account is successfully added")
                print(user.most_uses)
                time.sleep(1)
                Account.most_used(user)
        elif temp_account_id == 'Done' or temp_account_id == 'done':
            print(user.most_uses)
        else:
            print("The account id does not exist. Please try again")
            time.sleep(1)
            Account.most_used(user)

    def transfer(user):
        temp_accounts = {}
        while True:
            try:
                i = 1
                for key in user.accounts:
                    temp_account = user.accounts.get(key)
                    temp_accounts[i] = user.accounts.get(key)
                    print(str(i) + "- "+"Account name: " + str(temp_account.name) + "\n   Account kind: " + str(
                        temp_account.kind)+"\n   Account id: " + str(temp_account.id) + "\n   balance: " + str(temp_account.balance))
                    i += 1
                temp = int(input(
                    "Choose the account that you want to transfer the money from(enter the number): \n"))
            except ValueError:
                print("Value is not valid. Please try again.")
                time.sleep(1)
                continue
            else:
                break
        if int(temp) in range(1, i):
            first_account = temp_accounts.get(int(temp))
        else:
            print("not valid answer, try again.")
            time.sleep(1)
            Account.transfer(user)
        while True:
            while True:
                try:
                    print(
                        "Please choose the account that you want to trasfer the money to: ")
                    for j in range(len(user.most_uses)):
                        print(str(j+1) + "- " + str(user.most_uses[j]))
                    second_account_id = input(
                        'If it is not in the list above, write the account id yourself:\n')
                    int(second_account_id)
                except ValueError:
                    print("Value is not valid. Please try again.")
                    time.sleep(1)
                    continue
                else:
                    break
            if len(second_account_id) == 10:
                second_account_id = second_account_id
                break
            elif int(second_account_id) <= len(user.most_uses) and int(second_account_id) > 0:
                second_account_id = user.most_uses[int(
                    second_account_id) - 1]
                break
            else:
                print("Not valid answer. please try again.")
                time.sleep(1)
        second_account = Account.all_accounts.get(second_account_id)
        amount = int(input('How much do you wanna transfer:'))
        while True:
            password = input('Please enter your account password:')
            if first_account.password == password:
                break
            else:
                print("Password is incorrect. Try again")
        if amount > first_account.balance:
            print("Your account does not have enough money")
            print("OPTARION FAILED")
            time.sleep(1)
            input('Press eny botton to go back to menu page')
            user.menu()
        else:
            first_account.balance = first_account.balance - amount
            second_account.balance = second_account.balance + amount
            issue_tracking = ''.join(
                ["{}".format(randint(0, 9))for num in range(0, 10)])
            while issue_tracking in Account.issue_tracking_list:
                issue_tracking = ''.join(
                    ["{}".format(randint(0, 9))for num in range(0, 10)])
            Account.issue_tracking_list.append(issue_tracking)
        first_account.transaction[issue_tracking] = {
            "Action": "Withdraw", "from": first_account.id, "To": second_account.id, "Amount": amount}
        second_account.transaction[issue_tracking] = {
            "Action": "Deposit", "from": first_account.id, "To": second_account.id, "Amount": amount}
        user.accounts.update({first_account.name:  first_account})
        Account.all_accounts.update({first_account.id: second_account})
        user.accounts.update({second_account.name:  second_account})
        Account.all_accounts.update({second_account.id: second_account})
        input('Trasnfer has bees successfully done. please press any botton to go back to menu page')

    def pay_bill(user):
        temp_accounts = {}
        temp_bill_id = input('Enter bill id: ')
        temp_bill_pay = input('Enter bill pay: ')
        temp_bill_key = (temp_bill_id, temp_bill_pay)
        if bill.bills_dict.get(temp_bill_key):
            if bill.bills_dict.get(temp_bill_key).status == False:
                while True:
                    while True:
                        try:
                            i = 1
                            for key in user.accounts:
                                temp_account = user.accounts.get(key)
                                temp_accounts[i] = user.accounts.get(key)
                                print(str(i) + "- "+"Account name: " + str(temp_account.name) + "\n   Account kind: " + str(
                                    temp_account.kind)+"\n   Account id: " + str(temp_account.id) + "\n   balance: " + str(temp_account.balance))
                                i += 1
                            temp = int(input(
                                "Choose the account that you want pay the bill from: \n"))
                        except ValueError:
                            print("Value is not valid. Please try again.")
                            time.sleep(1)
                            continue
                        else:
                            break
                    if int(temp) in range(1, i):
                        account = temp_accounts.get(int(temp))
                        user.accounts.get(account.name).balance = user.accounts.get(
                            account.name).balance - bill.bills_dict.get(temp_bill_key).amount
                        bill.bills_dict.get(temp_bill_key).status = True
                        print("Bill successfull got paid")
                        issue_tracking = ''.join(
                            ["{}".format(randint(0, 9))for num in range(0, 10)])
                        while issue_tracking in Account.issue_tracking_list:
                            issue_tracking = ''.join(
                                ["{}".format(randint(0, 9))for num in range(0, 10)])
                        Account.issue_tracking_list.append(issue_tracking)
                        user.accounts.get(account.name).transaction[issue_tracking] = {
                            "Action": "Withdraw", "Bill Id and Bill Pay:": temp_bill_key, "Amount": bill.bills_dict.get(temp_bill_key).amount}
                        break
                    else:
                        print("not valid answer, try again.")
                        time.sleep(1)
            else:
                print("This bill has already been paid.")
        else:
            print("Invalid bill id or bill pay. Please try again")
            Account.pay_bill(user)
        input("Press any botton to go back to manu page.")

    def loan(user):
        if user.loan_status == False:
            print("Loan plan: ")
            print(
                "amount = 2000$ and for 10 month 220 will be withdraw from your account")
            today = date.today()
            temp_name = input(
                'Which account do you want to get the loan for(Enter the name):')
            user.accounts.get(temp_name).balance += 2000
            user.loan_month.append(10)
            user.loan_status = True
            print("Your loan is added to your account")
        else:
            if user.loan_month[0] > 0:
                if today.day == date.today():
                    user.accounts.get(temp_name).balance -= 220
                    user.loan_month[0] -= 1
                    if user.loan_month[0] == 0:
                        user.loan_status == False
        input("press any key to go back")

    def close(user):
        temp_accounts = {}
        while True:
            try:
                i = 1
                for key in user.accounts:
                    temp_account = user.accounts.get(key)
                    temp_accounts[i] = user.accounts.get(key)
                    print(str(i) + "- "+"Account name: " + str(temp_account.name) + "\n   Account kind: " + str(
                        temp_account.kind)+"\n   Account id: " + str(temp_account.id) + "\n   balance: " + str(temp_account.balance))
                    i += 1
                temp = int(input(
                    "Choose the account that you want to close: \n"))
            except ValueError:
                print("Value is not valid. Please try again.")
                time.sleep(1)
                continue
            else:
                break
        if int(temp) in range(1, i):
            first_account = temp_accounts.get(int(temp))
        else:
            print("not valid answer, try again.")
            time.sleep(1)
            Account.close(user)
        if user.accounts[first_account.name].balance != 0:
            print(
                'The account is not empty')
            time.sleep(1)
            user.accounts.pop(first_account.name, None)
        while True:
            try:
                i = 1
                for key in user.accounts:
                    temp_account = user.accounts.get(key)
                    temp_accounts[i] = user.accounts.get(key)
                    print(str(i) + "- "+"Account name: " + str(temp_account.name) + "\n   Account kind: " + str(
                        temp_account.kind)+"\n   Account id: " + str(temp_account.id) + "\n   balance: " + str(temp_account.balance))
                    i += 1
                second_account = int(input(
                    "Please choose another account to transfer the money to:\n"))
            except ValueError:
                print("Value is not valid. Please try again.")
                time.sleep(1)
                continue
            else:
                break
        if int(temp) in range(1, i):
            second_account = temp_accounts.get(int(temp))
        else:
            print("not valid answer, try again.")
            time.sleep(1)
            Account.close(user)
            user.accounts[second_account].balance += Account.all_accounts.get(
                first_account.id).balance
        Account.all_accounts.pop(first_account.id, None)
        print("Your account is successfully deleted")
        time.sleep(1)


bill_one = bill('1234', '12345')
bill_one.amount = 300
bill_one.status = False

bill_two = bill('1237', '12345')
bill_two.amount = 100
bill_two.status = False

first = Account('1234567890')
first.name = 'first'
first.balance = 300
first.password = '1234'
first.kind = 'Student account'
first.transaction['123456678'] = {
    'Action': 'Withdraw', 'from': '1234567890', 'To': '9857684396', 'Amount': 100}
first.transaction['098654345'] = {
    'Action': 'Withdraw', 'from': '1234567890', 'To': '9857684396', 'Amount': 100}
first.transaction['098765445'] = {
    'Action': 'Withdraw', 'from': '1234567890', 'To': '9857684396', 'Amount': 100}
Account.all_accounts['1234567890'] = first

second = Account('0123456789')
second.name = 'second'
second.balance = 300
second.password = '1234'
second.kind = 'Children account'
Account.all_accounts['0123456789'] = second

third = Account('5768594839')
third.name = 'third'
third.balance = 300
third.password = '1234'
third.kind = 'Student account'
Account.all_accounts['5768594839'] = third

fourth = Account('9857684396')
fourth.name = 'fourth'
fourth.balance = 300
fourth.password = '1234'
fourth.kind = 'Student account'
Account.all_accounts['9857684396'] = fourth

samin = User('2233445566', 'Samin')
samin.password = '123456'
samin.email = 'saminrazeghi@gmail.com'
samin.contact_number = '09125647568'
samin.accounts[first.name] = first
samin.accounts[second.name] = second
samin.accounts[third.name] = third
samin.most_uses = ['5768594839', '9857684396']
User.users_dict['2233445566'] = samin

amir = User('3344667755', 'amir')
amir.password = '123456'
amir.email = 'amiramir@gmail.com'
amir.contact_number = '09123465768'
amir.accounts[third.name] = third
amir.accounts[fourth.name] = fourth
amir.most_uses = ['1234567890', '0123456789']
User.users_dict['3344667755'] = amir


def start():
    print("\n        Welcome to the bank")
    flag = False
    while flag == False:
        account_existence = input('Do you already have an account(y/n): ')
        if account_existence == "y" or account_existence == "Y" or account_existence == "Yes" or account_existence == "yes":
            print("Log in:")
            User.login()
        elif account_existence == "No" or account_existence == "no" or account_existence == "n" or account_existence == "N":
            print("Registration:")
            User.register()
        else:
            print("\nNot valid answer.\nPleasn answer with yes or no.\nTry again.")
            time.sleep(0.5)


start()
