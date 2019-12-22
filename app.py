import json
import io
from budget import bills, gross_income, income
import pandas as pd

print('First we need to get some details from you before we start\n')

hours = input('Hours worked: ')
income = income.net_income(hours)

app = True

while app == True:
    print('''
#######################################
# What would you like to do?          #
# 1. See net earnings for period      #   
# 2. See money left over after bills  #
# 3. Add new bill(s)                  #
# 4. View bills                       #
# 5. Exit                             #
#######################################
    ''')

    response = input('Option 1-5: ')

    # For response #1
    if response == '1':
        print(income)
        menu = input("Would you like to return to the menu? \n")
        if menu == 'Y':
            app = True
        elif menu == 'N':
            app = False
        else:
            input('Your response was not valid please enter a valid response: \n')




    elif response == '2':
        remaining = bills.remaining(hours)
        print(remaining)
        menu = input("Would you like to return to the menu? \n")
        if menu == 'Y':
            app = True
        elif menu == 'N':
            app = False
        else:
            input('Your response was not valid please enter a valid response: \n')
        

    
    elif response == '3':
        bills.add_bill()
        menu = input("Would you like to return to the menu? \n")
        if menu == 'Y':
            app = True
        elif menu == 'N':
            app = False
        else:
            input('Your response was not valid please enter a valid response: \n')
    
    
    elif response == '4':
        df = pd.DataFrame.from_dict(bills.list_bills(), orient='index')
        print(df)
        menu = input("Would you like to return to the menu? \n")
        if menu == 'Y':
            app = True
        elif menu == 'N':
            app = False
        else:
            input('Your response was not valid please enter a valid response: \n')

